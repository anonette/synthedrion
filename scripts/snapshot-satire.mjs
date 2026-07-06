// Snapshot saved satirical takes into a self-contained static bundle so they can
// be replayed WITHOUT the backend running (offline Lovable fallback, static host).
//
// Reads from a running backend, downloads every referenced asset (head videos,
// portraits, per-turn audio), rewrites the URLs to local relative paths, and
// writes:
//   public/satire-archive/index.json            <- list of takes
//   public/satire-archive/{session_id}.json     <- one performance (local URLs)
//   public/satire-archive/heads/{actor}.{webm,png}
//   public/satire-archive/session-assets/{id}/satire-audio/turn-N.mp3
//
// Usage:
//   node scripts/snapshot-satire.mjs
//   $env:ROUNDTABLE_BASE_URL="https://aicoldwar.ngrok.app"; node scripts/snapshot-satire.mjs
import { mkdir, writeFile } from 'node:fs/promises';
import { join, dirname } from 'node:path';

const BASE = (process.env.ROUNDTABLE_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');
const OUT = process.env.SATIRE_ARCHIVE_DIR || join(process.cwd(), 'public', 'satire-archive');
const HEADERS = { 'ngrok-skip-browser-warning': 'true' };

async function getJSON(path) {
  const res = await fetch(BASE + path, { headers: HEADERS });
  if (!res.ok) throw new Error(`GET ${path} -> ${res.status}`);
  return res.json();
}

async function download(urlPath, destAbs) {
  const res = await fetch(BASE + urlPath, { headers: HEADERS });
  if (!res.ok) throw new Error(`GET ${urlPath} -> ${res.status}`);
  const buf = Buffer.from(await res.arrayBuffer());
  await mkdir(dirname(destAbs), { recursive: true });
  await writeFile(destAbs, buf);
  return buf.length;
}

const rel = (u) => (u || '').replace(/^\//, ''); // "/heads/x.webm" -> "heads/x.webm"

async function main() {
  await mkdir(OUT, { recursive: true });
  const { takes } = await getJSON('/api/satire-takes?limit=200');
  console.log(`[snapshot-satire] ${takes.length} take(s) from ${BASE}`);

  const fetched = new Set();
  const index = [];
  let assetCount = 0;

  for (const t of takes) {
    const rep = await getJSON(`/api/satire-replay/${t.session_id}`);
    for (const turn of rep.turns) {
      for (const key of ['head_video_url', 'portrait_url', 'audio_url']) {
        const u = turn[key];
        if (u && !fetched.has(u)) {
          fetched.add(u);
          try { await download(u, join(OUT, rel(u))); assetCount++; }
          catch (e) { console.warn(`  ! ${e.message}`); }
        }
        if (u) turn[key] = rel(u); // rewrite to local relative path
      }
    }
    await writeFile(join(OUT, `${t.session_id}.json`), JSON.stringify(rep, null, 2));
    index.push({
      session_id: t.session_id, prompt: t.prompt, mode: t.mode,
      count: t.count, preview: t.preview, replay_file: `${t.session_id}.json`,
    });
    console.log(`  + ${t.session_id} (${rep.turns.length} turns)`);
  }

  await writeFile(join(OUT, 'index.json'), JSON.stringify({ total: index.length, takes: index }, null, 2));
  console.log(`[snapshot-satire] wrote ${index.length} take(s) + ${assetCount} asset(s) -> ${OUT}`);
}

main().catch((e) => { console.error('[snapshot-satire]', e); process.exit(1); });

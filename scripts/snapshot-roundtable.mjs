import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, '..');

const baseUrl = (process.env.ROUNDTABLE_BASE_URL || 'http://127.0.0.1:8000').replace(/\/$/, '');
const outRoot = path.join(repoRoot, 'public', 'roundtable-archive');
const replayRoot = path.join(outRoot, 'replay');

async function fetchJson(url) {
  const res = await fetch(url, {
    headers: {
      'ngrok-skip-browser-warning': 'true',
      'Accept': 'application/json',
    },
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`${res.status} ${res.statusText} for ${url}\n${body}`);
  }

  return await res.json();
}

async function writeJson(filePath, value) {
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, `${JSON.stringify(value, null, 2)}\n`, 'utf8');
}

async function main() {
  console.log(`[roundtable] snapshot source: ${baseUrl}`);

  const current = await fetchJson(`${baseUrl}/weekly/current`);
  const archive = await fetchJson(`${baseUrl}/weekly/archive?limit=50&offset=0`);

  await mkdir(replayRoot, { recursive: true });
  await writeJson(path.join(outRoot, 'current.json'), current);
  await writeJson(path.join(outRoot, 'archive.json'), archive);

  const sessionIds = new Set();
  if (current?.session_id) {
    sessionIds.add(current.session_id);
  }
  for (const item of archive?.items || []) {
    if (item?.session_id) {
      sessionIds.add(item.session_id);
    }
  }

  let replayCount = 0;
  for (const sessionId of sessionIds) {
    const replay = await fetchJson(`${baseUrl}/api/replay/${sessionId}`);
    await writeJson(path.join(replayRoot, `${sessionId}.json`), replay);
    replayCount += 1;
  }

  console.log(`[roundtable] wrote current.json`);
  console.log(`[roundtable] wrote archive.json`);
  console.log(`[roundtable] wrote ${replayCount} replay file(s)`);
  console.log(`[roundtable] output: ${outRoot}`);
}

main().catch((error) => {
  console.error('[roundtable] snapshot failed');
  console.error(error instanceof Error ? error.stack : error);
  process.exitCode = 1;
});

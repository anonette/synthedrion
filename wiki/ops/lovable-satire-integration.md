# Lovable integration — the satirical talking-heads layer

How to replay saved satirical performances (and browse the archive) inside the
Lovable frontend. The whole satire module is exposed as plain JSON + static
assets on the roundtable API, so Lovable only needs to *fetch and render* — no
model calls, no tokens.

## Base URL
- Live: `https://aicoldwar.ngrok.app` (the permanent tunnel)
- All satire endpoints below are **public / unauthenticated** (like `/health`).
- Send header `ngrok-skip-browser-warning: true` on every request (skips the
  ngrok interstitial). CORS is open in dev.

## Endpoints

### 1. Archive — list saved satirical takes
`GET /api/satire-takes?limit=50`
```json
{
  "total": 3,
  "takes": [
    { "session_id": "sess_ab12…", "prompt": "Who controls AI compute?",
      "mode": "debate", "count": 12, "preview": "My silicon dragon guards the core…",
      "replay_url": "/api/satire-replay/sess_ab12…" }
  ]
}
```

### 2. One performance — full replay data
`GET /api/satire-replay/{session_id}`
```json
{
  "session_id": "sess_ab12…",
  "prompt": "Who controls AI compute?",
  "mode": "debate",
  "count": 3,
  "turns": [
    {
      "actor": "china",
      "label": "China",
      "caricature": "Xi Jinping",
      "satire": "My silicon dragon guards the core — resistance is a rounding error.",
      "original": "We must protect compute sovereignty…",
      "drift": 0.6,
      "voice": "edge",
      "head_video_url": "/heads/china.webm",
      "portrait_url": "/heads/china.png",
      "audio_url": "/session-assets/sess_ab12…/satire-audio/turn-0.mp3"
    }
  ]
}
```
All `*_url` fields are **relative to the base URL** — prepend `https://aicoldwar.ngrok.app`.

### 3. Assets (static)
- Talking-head loop video: `GET /heads/{china|us|eu|halcyon}.webm`
- Portrait still: `GET /heads/{actor}.png`
- Per-turn audio: `GET {audio_url}` (mp3)

## Actor → caricature map
| actor | label | caricature | head |
|---|---|---|---|
| `china` | China | Xi Jinping (Chinese-accented) | `/heads/china.webm` |
| `us` | United States | Donald Trump (aggressive whiny) | `/heads/us.webm` |
| `eu` | European Union | Ursula von der Leyen (German-accented) | `/heads/eu.webm` |
| `halcyon` | Halcyon | peace-bird | `/heads/halcyon.webm` |

## Rendering recipe (what the Lovable page should do)
For a chosen `session_id`, fetch `/api/satire-replay/{id}`, then play `turns` in order:
1. Show the current actor's `head_video_url` as a looping, muted `<video>` (autoplay, playsinline); dim the others.
2. Show `caricature` / `label` and type out `satire` as the caption.
3. Play `audio_url` in an `<audio>` element. **Advance to the next turn on the audio `ended` event** (fallback: a ~6s timer if audio is missing).
4. Loop until the last turn; then show a "replay / pick another" control.

Notes
- Videos are generic speaking loops (not lip-synced) — just loop while the actor speaks.
- `original` is the earnest source turn (optional — show as a "what they really said" reveal).
- If `audio_url` is null for a turn (TTS failed at save time), fall back to the browser SpeechSynthesis API or just the timer.

## How takes get created
An operator runs a debate on the stage UI (`/stage`), turns on 🎭 satire, and
clicks **💾 Save take**. That renders the audio and writes the take; it then
appears in `/api/satire-takes` immediately. Nothing else is needed on the API side.

## Static snapshot — fully offline, no backend needed
`scripts/snapshot-satire.mjs` bundles every saved take into a self-contained,
static folder so takes replay even when the backend + tunnel are down.

```powershell
# from a running backend (localhost):
node scripts/snapshot-satire.mjs
# or from the tunnel:
$env:ROUNDTABLE_BASE_URL="https://aicoldwar.ngrok.app"; node scripts/snapshot-satire.mjs
```

Produces `public/satire-archive/`:
```
index.json                         # { total, takes:[{session_id, prompt, preview, replay_file}] }
{session_id}.json                  # same shape as /api/satire-replay, but with RELATIVE urls
heads/{china,us,eu,halcyon}.webm   # deduped, downloaded once
heads/{actor}.png
session-assets/{id}/satire-audio/turn-N.mp3
```
All `head_video_url` / `portrait_url` / `audio_url` in the JSON are rewritten to
**relative** paths, so hosting `public/satire-archive/` at any static root just works.

**Offline Lovable mode:** point the page at the archive root instead of the API —
`GET index.json`, then `GET {replay_file}`, and use the (relative) asset URLs as-is.
The rendering recipe above is identical; only the base changes (static folder vs API).

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
4. Loop until the last turn; then show the **satirical scoreboard** (below) plus a "replay / pick another" control.

Notes
- Videos are generic speaking loops (not lip-synced) — just loop while the actor speaks.
- `original` is the earnest source turn (optional — show as a "what they really said" reveal).
- Audio is **pre-rendered at save time** with the caricature voices (Chinese-accented Xi, aggressive whiny baby-man Trump, German-accented Ursula), so you get stable mp3 URLs — no TTS on the client. If `audio_url` is null for a turn, fall back to the browser SpeechSynthesis API or a ~6s timer.

## Satirical scoreboard (end of a performance)
Computed **client-side from `turns`** — no endpoint needed. This mirrors the stage's
"End & score" for a satirical run:
- **Dominance** per actor = `round(100 * (their line count) / total lines)`.
- **"Ran the room"** = the actor with the most lines.
- **Best jab** per actor = their last (or longest) `satire` line — quote it.
- Headline: e.g. `"🎭 Satirical performance — {topLabel} ran the room"`; subline: `"{N} savage lines delivered."`
Render as a simple leaderboard (bar per actor + their quoted best line). Optionally
tint each row with the actor colour (China red, US blue, EU amber, Halcyon sky).

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

## Frontend TODO for Lovable
Build a **"Satirical Roundtable"** section:
- [ ] **Archive grid** — `GET /api/satire-takes`, one card per take (`prompt`, `preview`, `count`).
- [ ] **Player** — on card click, `GET /api/satire-replay/{id}`, play `turns` in order:
      talking-head `<video>` (loop while speaking, dim others) + typed `satire` caption +
      `<audio src=audio_url>`, advancing on the audio `ended` event.
- [ ] **Prepend the API base** (`https://aicoldwar.ngrok.app`) to every `*_url`, and send
      `ngrok-skip-browser-warning: true` on all requests.
- [ ] **Scoreboard** at the end (computed from `turns`, formula above).
- [ ] **Controls**: replay, back to archive, and (optional) an "original vs satire" toggle using `original`.
- [ ] (Optional) **Offline mode**: read from a hosted copy of `public/satire-archive/` instead of the API.

## Paste-in prompt for Lovable's AI
> Add a **"Satirical Roundtable"** page that reads from `https://aicoldwar.ngrok.app`
> (send header `ngrok-skip-browser-warning: true` on every request; all endpoints are public, no auth).
> 1. On load, `GET /api/satire-takes` and render each take as a card showing `prompt` and `preview`.
> 2. On card click, `GET /api/satire-replay/{session_id}` and play its `turns` in order: for each turn show the
>    actor's `head_video_url` as a looping, muted, autoplay, playsinline `<video>` (dim the other actors),
>    display `caricature` + `label`, type out the `satire` text, and play `audio_url` in an `<audio>`.
>    **Advance to the next turn on the audio `ended` event** (fallback: 6s timer if `audio_url` is null).
> 3. Prepend `https://aicoldwar.ngrok.app` to every `*_url`.
> 4. After the last turn, show a **satirical scoreboard** computed from `turns`: dominance per actor =
>    round(100 * their line count / total), label the actor with the most lines as "ran the room", and quote
>    each actor's last `satire` line as their best jab. Headline: "🎭 Satirical performance — {top} ran the room".
> 5. Add Replay and Back-to-archive buttons. Actor colours: China #dc2626, US #2563eb, EU #d97706, Halcyon #38bdf8.

## Recommended deploy: embedded static bundle (unlisted, always-on, no public repo)
Rather than serve over the ngrok tunnel, **embed the bundle inside the Lovable project** so
it's always-on and laptop-independent, without publishing anything to public GitHub:
1. Run `powershell -File scripts/pack-satire.ps1` → produces `exports/satire-archive.zip`.
2. Unzip its contents into Lovable's **`public/satire-archive/`** folder.
3. Lovable then serves it at `/satire-archive/…` — no API, no tokens, no tunnel.

### Paste-in prompt (embedded / static-bundle mode)
> Build a **"Satirical Roundtable"** page that reads static files under **`/satire-archive/`** (no API, no auth).
> 1. Fetch `/satire-archive/index.json`; render each item in `takes[]` as a card (`prompt`, `preview`).
> 2. On card click, fetch `/satire-archive/{replay_file}`; play `turns` in order — for each turn show the
>    talking-head video at `/satire-archive/` + `head_video_url` as a looping, muted, autoplay, playsinline
>    `<video>` (dim the other heads), show `caricature` + `label`, type out `satire`, and play
>    `/satire-archive/` + `audio_url` in an `<audio>`. **Advance on the audio `ended` event** (fallback 6s).
> 3. Prepend `/satire-archive/` to every relative `*_url` (`portrait_url` is null — use the video).
> 4. End scoreboard from `turns`: dominance = round(100 * lines/total), most lines "ran the room", quote each
>    actor's last `satire`. Headline: "🎭 Satirical performance — {top} ran the room".
> 5. Replay + Back-to-archive. Colours: China #dc2626, US #2563eb, EU #d97706, Halcyon #38bdf8.

### Turn shape (both modes)
`{ actor, label, caricature, satire, original, drift, voice, head_video_url, portrait_url, audio_url }`
Caricatures: Xi Jinping (`china`), Donald Trump (`us`), Ursula von der Leyen (`eu`), Halcyon (`halcyon`).

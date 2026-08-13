# Lovable update prompt — 2026-08-14 (b): Live Event menu, live session page, clean prompts

Paste this whole block into Lovable in one go. Skip any item already done.

---

Backend base `https://aicoldwar.ngrok.app`; always send header `ngrok-skip-browser-warning: true`; render from endpoints, never hardcode.

**1. "Live Event" leads the menu.** Add it first and visually dominant (accent pill): **Live Event · About · Who's Who · Weekly Roundtable · Mirror World · Satirical Roundtable · Archive**. The page: (a) hero event banner from `GET /event` ("📅 Roundtable — Thursday 10 September 2026, 9:00–10:30 (Europe/Warsaw) · C-7, room 3.09, Kraków, Poland"; `status` is empty — show nothing beneath); (b) a "What happens in the room" section: the three state actors debate live on their own models, guests can be summoned mid-debate (names/archetypes from `GET /roster`), and the audience speaks directly to the agents — spoken questions are transcribed into the debate and the agents answer aloud in their own voices; (c) a compact teaser row of participant names linking to Who's Who; (d) a "watch live" slot linking to the Live Session page (item 2).

**2. Rebuild "Join the live session" as a real Live Session page** (it currently dead-ends at a weekly replay):
- Find the live session: `GET /sessions/recent?limit=10`, most recent entry with `status: "running"`; if none, show "no live session right now" linking to the latest replay.
- Watch live: poll `GET /session/{id}` every 5 seconds, appending new transcript turns with the same renderers as replays (archivist shelf cards; `kind: "human"` turns render as "from the floor").
- Host controls (keep behind the same operator gating used for starting sessions): "Continue debate ▶" → `POST /session/message {session_id}`; the summon buttons (Halcyon / James / Archivist with logic picker); and "🎙 Speak to the agents" hold-to-talk: record mic audio (MediaRecorder webm/opus), POST the raw blob to `POST /session/{id}/listen?speaker=audience` (blob's Content-Type header + operator token), render the returned `transcript` as a floor turn, then request the reply via `POST /session/message` with optional `{actor}` from a "who answers" dropdown (or a guest summon endpoint), and speak it by POSTing `{actor, text, provider: "edge"}` to `/tts` and playing the base64 `audio_b64`.
- Optional voice for the watch view: when a new agent turn arrives, fetch its audio the same `/tts` way and play it, with a mute toggle.

**3. Prompts are clean now — just refetch.** The backend no longer exposes internal steering text ("[The next actor to speak MUST...]", "Spoken from the floor (...)") in any public prompt field — weekly cards, recent sessions, session view, and replays all show only the original question. Remove any client-side workarounds and re-render from the endpoints. Floor questions still appear where they belong: as turns in the transcript.

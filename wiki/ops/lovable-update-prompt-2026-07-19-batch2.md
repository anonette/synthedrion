# Lovable update prompt — batch 2

Paste this whole block into Lovable in one go.

---

Several fixes and additions to the roundtable frontend:

**1. Simplify the mode menu.** Drop "Negotiation", "Crisis", and "Policy-planning" from the mode picker — they're prompt-tone variants of the same plain debate turns, not structurally distinct, so they read as broken/inactive. Keep only **Debate**, **Propaganda Lab**, and **Mirror World** as top-level modes — these three actually produce different output shapes (plain turns, structured poster artifacts, three-layer cards).

**2. Propaganda Lab poster rendering.** This mode is fully functional server-side (verified: returns complete metadata — `slogan`, `commentary`, `artifact_type`, `image_prompt` — plus a real generated image), but if posters aren't showing up, it's a rendering/binding bug like the mirror-turn one below. Bind `metadata.image_url` (a `data:image/jpeg;base64,...` URI), `metadata.slogan`, and `metadata.commentary` to an actual poster card. Also: these image payloads are large (~1MB+ per poster) — don't try to hold many of them in memory/local-storage at once; load them lazily per visible card.

**3. Mirror-turn card data-binding** (if not already fixed): for turns where `metadata.format === "mirror-turn"`, bind `metadata.official_line` → "Official line", `metadata.buried_reality` → "Buried reality", `metadata.speculation` → "Mirror (speculation)", and `metadata.irony` as a labeled caption — not stray unlabeled text.

**4. Show the seed incident as a clean header.** Every mirror-world session response (`POST /session/start` and `GET /api/replay/{id}`) now includes a structured `incident` object: `{id, target, state, group, confidence, amount_usd, asset, vector, timestamp}`. Render this as a clear "Incident:" header at the top of the mirror-world session view (e.g. "Incident: Tornado Cash Governance — $750,000, DPRK/Lazarus Group, confidence 0.18") instead of leaving it buried in the prose seed text. This directly fixes "not clear what the incident is."

**5. Mirror World needs the same Live/Archive split as the Weekly Roundtable.** Give the dedicated Mirror World page (from the earlier "make it a separate page" fix) its own "Live Session Studio" / "Archive & Replay" tabs, mirroring the weekly roundtable's structure — right now it's unclear whether you're starting a new incident session or looking at a past one.

**6. Guest voices should link to their own feeds.** On the Who's Who page, make Halcyon's and James's cards clickable through to their own feed pages: Halcyon → `GET /halcyon/good-news` (his ledger of hopeful stories he's found — title, source, why_hopeful, url), James → `GET /james/takes` (every take he's left, newest first, linking back to the originating session). Both are public GET endpoints, no auth. Style them distinctly (Halcyon warm/hopeful, James dark/cynical) matching their personas.

**7. Clean up the replay controls.** The current replay panel has unclear/unlabeled buttons ("Full", "Per-event", "Showcase", "Forensic", "Live", "Close") and some do nothing when clicked. Audit these: remove any that aren't wired to real functionality, and label the ones that remain in plain language (e.g. "Play full replay" vs "Step through turn-by-turn" instead of "Full" / "Per-event").

**8. Loading-state copy for slow AI calls** (if not already done): anything waiting on a fresh backend AI response (new turn, mirror-card, James's take, propaganda poster) should say something like "Generating... usually takes under a minute" rather than a bare spinner — these calls genuinely take 30-60 seconds from the model provider, this is expected, not broken.

---

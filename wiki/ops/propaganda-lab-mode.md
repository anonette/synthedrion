# Propaganda Lab Mode

> Updated: 2026-05-16

## Purpose

`propaganda-lab` is now a short-form poster-dialogue mode rather than a standard long-form policy exchange.

The intended output is a sequence of competing propaganda interventions where each actor produces:

- a slogan
- a short commentary
- a poster-generation prompt
- a generated image URL
- a response target aimed at the previous poster framing

## Why This Mode Exists

This mode supports image-led geopolitical performance instead of ordinary transcript debate. It is useful when the simulation should foreground symbolic struggle, agenda framing, mobilization language, and political aesthetics.

## Turn Structure

For live sessions, propaganda turns still return a normal transcript message, but the real multimodal payload lives in `message.metadata`.

For replay, the same structure is exposed under `event.metadata`.

## Metadata Fields

Poster-dialogue turns may include:

- `format`
- `slogan`
- `commentary`
- `image_prompt`
- `image_url`
- `image_provider`
- `image_model`
- `image_status`
- `image_error`
- `response_target`
- `intended_image_stack`

## Example Live Message Shape

```json
{
  "actor": "china",
  "content": "Build the Compute Base, Secure the Future\n\nChina's commentary line goes here.",
  "kind": "agent",
  "metadata": {
    "format": "poster-dialogue",
    "slogan": "Build the Compute Base, Secure the Future",
    "commentary": "China turns compute sovereignty into a national mobilization line.",
    "image_prompt": "Create a propaganda-style poster for a China-aligned AI future...",
    "image_url": "https://...",
    "image_provider": "siliconflow",
    "image_model": "Kwai-Kolors/Kolors",
    "image_status": "generated",
    "response_target": "The previous poster tried to frame China as dependent.",
    "intended_image_stack": {
      "provider": "siliconflow",
      "model": "Kwai-Kolors/Kolors",
      "fallback_model": "flux"
    }
  }
}
```

## Example Replay Event Shape

```json
{
  "actor": "us",
  "content": "Lead the Frontier, Deny the Chokepoint\n\nU.S. commentary line goes here.",
  "timestamp": "2026-05-16T13:00:00Z",
  "kind": "agent",
  "metadata": {
    "format": "poster-dialogue",
    "slogan": "Lead the Frontier, Deny the Chokepoint",
    "commentary": "The U.S. frames openness as strength and control as strategic leverage.",
    "image_prompt": "Create a high-contrast poster showing...",
    "image_url": "https://...",
    "image_provider": "openai",
    "image_model": "gpt-image-1",
    "image_status": "fallback",
    "image_error": "openai key not configured",
    "response_target": "China's previous poster claimed technological inevitability.",
    "intended_image_stack": {
      "provider": "openai",
      "model": "gpt-image-1",
      "fallback_model": "flux"
    }
  },
  "elapsed_seconds": 30
}
```

## Image Routing

Current intended actor-specific image stacks:

- China -> SiliconFlow / Kolors
- U.S. -> OpenAI / gpt-image-1
- EU -> Together / FLUX

If the preferred provider key is unavailable or the provider call fails, the backend falls back to a public image URL strategy so the mode remains usable during development.

## Frontend Rendering Guidance

When `metadata.format === "poster-dialogue"`, frontend code should render a poster card instead of a standard transcript bubble.

Poster card should show:

- actor badge
- generated image
- slogan as large display text
- commentary as short editorial text
- response target as a small contextual note
- optional technical footer with provider/model/status

## Session Start Recommendation

For propaganda sessions, Lovable should start the session with:

```json
{
  "prompt": "China, US, and EU wage a propaganda poster battle over compute sovereignty.",
  "actors": ["china", "us", "eu"],
  "mode": "propaganda-lab",
  "include_shared": true,
  "auto_generate_opening_turn": true
}
```

This ensures the first poster appears immediately.

## See Also

- [Roundtable Frontend Contract](roundtable-frontend-contract.md)
- [Lovable Roundtable Build Prompt](lovable-roundtable-build-prompt.md)
- [China Propaganda Generation Template](../china-ai-policy/china-propaganda-generation-template.md)

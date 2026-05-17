from __future__ import annotations

import base64
from urllib.parse import quote

import httpx

from .config import ACTOR_IMAGE_MODELS, OPENAI_API_KEY, OPENROUTER_API_KEY, OPENROUTER_APP_NAME, OPENROUTER_BASE_URL, OPENROUTER_SITE_URL, SILICONFLOW_API_KEY, TOGETHER_API_KEY


def image_model_config(actor: str) -> dict[str, str]:
    return ACTOR_IMAGE_MODELS[actor]


async def generate_actor_image(actor: str, image_prompt: str) -> dict[str, str]:
    config = image_model_config(actor)
    provider = config["provider"]
    model = config["model"]

    try:
        if provider == "openrouter" and OPENROUTER_API_KEY:
            return await _generate_openrouter_image(model, image_prompt)
        if provider == "openai" and OPENAI_API_KEY:
            return await _generate_openai_image(model, image_prompt)
        if provider == "siliconflow" and SILICONFLOW_API_KEY:
            return await _generate_siliconflow_image(model, image_prompt)
        if provider == "together" and TOGETHER_API_KEY:
            return await _generate_together_image(model, image_prompt)
    except Exception as exc:
        return _pollinations_fallback(config["fallback_model"], image_prompt, f"{provider} failed: {exc}")

    return _pollinations_fallback(config["fallback_model"], image_prompt, f"{provider} key not configured")


async def _generate_openrouter_image(model: str, prompt: str) -> dict[str, str]:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ],
            }
        ],
        "modalities": ["image"],
    }
    async with httpx.AsyncClient(timeout=120.0) as client:
        res = await client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    image_url = _extract_openrouter_image_url(data)
    if not image_url:
        raise RuntimeError(f"OpenRouter image response did not include an image payload: {data}")
    return {
        "image_url": image_url,
        "image_provider": "openrouter",
        "image_model": model,
        "image_status": "generated",
    }


def _extract_openrouter_image_url(data: dict) -> str | None:
    def from_part(part: dict) -> str | None:
        image_url = part.get("image_url")
        if isinstance(image_url, dict):
            return image_url.get("url")
        if isinstance(image_url, str):
            return image_url

        if part.get("type") == "image_url" and isinstance(part.get("url"), str):
            return part["url"]

        b64 = part.get("b64_json") or part.get("image_base64") or part.get("data")
        if isinstance(b64, str) and b64:
            if b64.startswith("data:image"):
                return b64
            return f"data:image/png;base64,{b64}"
        return None

    for item in data.get("data", []):
        if isinstance(item, dict):
            url = item.get("url")
            if isinstance(url, str) and url:
                return url
            url = from_part(item)
            if url:
                return url

    choices = data.get("choices", [])
    for choice in choices:
        message = choice.get("message", {}) if isinstance(choice, dict) else {}
        content = message.get("content")
        if isinstance(content, list):
            for part in content:
                if isinstance(part, dict):
                    url = from_part(part)
                    if url:
                        return url
        elif isinstance(content, dict):
            url = from_part(content)
            if url:
                return url

        images = message.get("images") or choice.get("images")
        if isinstance(images, list):
            for image in images:
                if isinstance(image, dict):
                    url = from_part(image)
                    if url:
                        return url
                elif isinstance(image, str):
                    return image

    return None


async def _generate_openai_image(model: str, prompt: str) -> dict[str, str]:
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "size": "1024x1024",
    }
    async with httpx.AsyncClient(timeout=90.0) as client:
        res = await client.post("https://api.openai.com/v1/images/generations", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    image_url = data["data"][0].get("url")
    if not image_url:
        raise RuntimeError("OpenAI image response did not include a URL")
    return {"image_url": image_url, "image_provider": "openai", "image_model": model, "image_status": "generated"}


async def _generate_siliconflow_image(model: str, prompt: str) -> dict[str, str]:
    headers = {
        "Authorization": f"Bearer {SILICONFLOW_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "image_size": "1024x1024",
    }
    async with httpx.AsyncClient(timeout=90.0) as client:
        res = await client.post("https://api.siliconflow.cn/v1/images/generations", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    image_url = data.get("images", [{}])[0].get("url") or data.get("data", [{}])[0].get("url")
    if not image_url:
        raise RuntimeError("SiliconFlow image response did not include a URL")
    return {"image_url": image_url, "image_provider": "siliconflow", "image_model": model, "image_status": "generated"}


async def _generate_together_image(model: str, prompt: str) -> dict[str, str]:
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "prompt": prompt,
        "width": 1024,
        "height": 1024,
        "steps": 4,
    }
    async with httpx.AsyncClient(timeout=90.0) as client:
        res = await client.post("https://api.together.xyz/v1/images/generations", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    image_url = data.get("data", [{}])[0].get("url")
    if not image_url:
        raise RuntimeError("Together image response did not include a URL")
    return {"image_url": image_url, "image_provider": "together", "image_model": model, "image_status": "generated"}


def _pollinations_fallback(model: str, prompt: str, reason: str) -> dict[str, str]:
    encoded = quote(prompt, safe="")
    image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&model={quote(model, safe='')}"
    return {
        "image_url": image_url,
        "image_provider": "pollinations-fallback",
        "image_model": model,
        "image_status": "fallback",
        "image_error": reason,
    }

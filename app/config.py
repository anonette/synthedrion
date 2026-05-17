from pathlib import Path
import os

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
WIKI_ROOT = PROJECT_ROOT / "wiki"

load_dotenv(PROJECT_ROOT / ".env")

ACTOR_HUBS = {
    "china": WIKI_ROOT / "china-ai-policy" / "china-ai-knowledge-base-hub.md",
    "us": WIKI_ROOT / "us-ai-policy" / "us-ai-knowledge-base-hub.md",
    "eu": WIKI_ROOT / "eu-ai-policy" / "eu-ai-knowledge-base-hub.md",
}

SHARED_HUB = WIKI_ROOT / "shared-ai-geopolitics" / "shared-ai-geopolitics-and-governance.md"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OPENROUTER_APP_NAME = os.getenv("OPENROUTER_APP_NAME", "AI Cold War Local Runtime")
OPENROUTER_SITE_URL = os.getenv("OPENROUTER_SITE_URL", "http://127.0.0.1:8000")

ACTOR_MODELS = {
    "china": os.getenv("OPENROUTER_MODEL_CHINA", "deepseek/deepseek-chat-v3-0324"),
    "us": os.getenv("OPENROUTER_MODEL_US", "openai/gpt-4.1-mini"),
    "eu": os.getenv("OPENROUTER_MODEL_EU", "mistralai/mistral-large-2411"),
}

ACTOR_IMAGE_MODELS = {
    "china": {
        "provider": os.getenv("IMAGE_PROVIDER_CHINA", "openrouter"),
        "model": os.getenv("IMAGE_MODEL_CHINA", "bytedance-seed/seedream-4.5"),
        "fallback_model": os.getenv("IMAGE_FALLBACK_MODEL_CHINA", "flux"),
    },
    "us": {
        "provider": os.getenv("IMAGE_PROVIDER_US", "openrouter"),
        "model": os.getenv("IMAGE_MODEL_US", "openai/gpt-5.4-image-2"),
        "fallback_model": os.getenv("IMAGE_FALLBACK_MODEL_US", "flux"),
    },
    "eu": {
        "provider": os.getenv("IMAGE_PROVIDER_EU", "openrouter"),
        "model": os.getenv("IMAGE_MODEL_EU", "black-forest-labs/flux.2-max"),
        "fallback_model": os.getenv("IMAGE_FALLBACK_MODEL_EU", "flux"),
    },
}

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY", "")

ALLOWED_PATH_PREFIXES = {
    "china": [
        WIKI_ROOT / "china-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
    ],
    "us": [
        WIKI_ROOT / "us-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
    ],
    "eu": [
        WIKI_ROOT / "eu-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
    ],
}

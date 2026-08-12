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
    "eu": os.getenv("OPENROUTER_MODEL_EU", "mistralai/ministral-14b-2512"),
}

# Model used for the end-of-debate recap and scoreboard. Defaults to the U.S. actor model.
RECAP_MODEL = os.getenv("OPENROUTER_MODEL_RECAP", ACTOR_MODELS["us"])

# Model used for the lightweight per-turn live "pulse" analysis. Keep it small/fast.
PULSE_MODEL = os.getenv("OPENROUTER_MODEL_PULSE", ACTOR_MODELS["us"])

# Model used for The Analyst's closing take (the cynical crypto-native counter-prediction).
JAMES_MODEL = os.getenv("OPENROUTER_MODEL_JAMES", RECAP_MODEL)

# Backup model for Halcyon when the primary CERIT endpoint is unavailable — a real model
# call, not canned text, so his voice degrades to a different brain, never to fabrication.
HALCYON_FALLBACK_MODEL = os.getenv("OPENROUTER_MODEL_HALCYON_FALLBACK", RECAP_MODEL)

# Model for The Critical Archivist's interventions. Its offline fallback is honest by
# construction (built from a real reorganization of the wiki corpus), so no backup model.
ARCHIVIST_MODEL = os.getenv("OPENROUTER_MODEL_ARCHIVIST", RECAP_MODEL)

# The Critical Archivist's own knowledge base (critical archival studies source notes).
# Deliberately NOT in ACTOR_HUBS/ALLOWED_PATH_PREFIXES: the Archivist is a summonable
# meta-agent, not a round-robin actor, and it loads this folder directly.
ARCHIVIST_HUB_DIR = WIKI_ROOT / "critical-archives"

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

# Image model for the mirror-world tabloid front page. Newspapers are text-heavy, so a
# GPT-image-class model that renders legible headlines beats photoreal diffusion here.
MIRROR_VISUAL_MODEL = os.getenv("MIRROR_VISUAL_MODEL", ACTOR_IMAGE_MODELS["us"]["model"])

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")
SILICONFLOW_API_KEY = os.getenv("SILICONFLOW_API_KEY", "")

ALLOWED_PATH_PREFIXES = {
    "china": [
        WIKI_ROOT / "china-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
        WIKI_ROOT / "ai-infrastructure",
    ],
    "us": [
        WIKI_ROOT / "us-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
        WIKI_ROOT / "ai-infrastructure",
    ],
    "eu": [
        WIKI_ROOT / "eu-ai-policy",
        WIKI_ROOT / "shared-ai-geopolitics",
        WIKI_ROOT / "geopolitics",
        WIKI_ROOT / "ai-governance",
        WIKI_ROOT / "ai-infrastructure",
    ],
}

# --- Halcyon: the summonable peace-builder ---------------------------------
# Halcyon is NOT a round-robin actor. It is injected on demand ("summoned") and
# runs on the free CERIT proxy (OpenAI-compatible /v1), separate from OpenRouter,
# so China/US/EU behaviour is untouched. It draws its "cool news" from the
# positive-stories ledger the Halcyon crawler fills.
HALCYON_MODEL = os.getenv("HALCYON_MODEL", "mistral-medium-3.5")
HALCYON_BASE_URL = os.getenv("HALCYON_BASE_URL", "https://agenthymia-llm.dyn.cloud.e-infra.cz/v1")
HALCYON_API_KEY = os.getenv("HALCYON_API_KEY", "")
HALCYON_LEDGER_PATH = os.getenv(
    "HALCYON_LEDGER_PATH",
    str(PROJECT_ROOT / "halcyon" / "positive-stories.md"),
)

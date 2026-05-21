from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_ARTICLES = PROJECT_ROOT / "raw" / "articles"
RAW_REG_DOCS = PROJECT_ROOT / "raw" / "reg-documents"
RAW_FOCUS_ROOT = PROJECT_ROOT / "raw" / "focus-issues"
SESSIONS_DIR = PROJECT_ROOT / "sessions"
STATE_PATH = SESSIONS_DIR / "news-ingest-state.json"
REPORT_PATH = SESSIONS_DIR / "news-ingest-report.md"

load_dotenv(PROJECT_ROOT / ".env")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", os.getenv("SERAPI", ""))

TOPIC_QUERIES = {
    "geopolitics": [
        "AI geopolitics China US EU latest news",
        "AI strategic rivalry China United States Europe",
    ],
    "policy": [
        "China AI regulation site:gov.cn OR site:cac.gov.cn OR site:miit.gov.cn",
        "US AI export controls BIS NIST White House AI policy",
        "EU AI Act cloud sovereignty site:europa.eu AI policy",
    ],
    "industry": [
        "Nvidia Huawei Meta OpenAI Google Microsoft AI industry signal",
        "ASML TSMC AI compute cloud latest news",
    ],
    "open-models": [
        "open-weight AI models geopolitics latest",
        "DeepSeek Qwen Llama Mistral open-source AI policy",
        "open model licensing AI government reaction",
    ],
    "chips-compute": [
        "AI chip controls compute sovereignty China US EU latest news",
        "cloud dependence AI sovereignty latest",
    ],
    "acquisitions": [
        "AI acquisition sovereignty Meta Manus latest",
        "AI merger national security review latest",
    ],
}

GOVERNMENT_DOMAINS = {
    "gov.cn", "cac.gov.cn", "miit.gov.cn", "ndrc.gov.cn", "zfxxgk.ndrc.gov.cn",
    "whitehouse.gov", "bis.doc.gov", "nist.gov", "europa.eu", "ec.europa.eu",
    "europarl.europa.eu", "consilium.europa.eu",
}

INDUSTRY_HINTS = {
    "openai.com", "anthropic.com", "meta.com", "about.fb.com", "nvidia.com", "huawei.com",
    "bytedance.com", "tencent.com", "alibabagroup.com", "asml.com", "tsmc.com",
    "mistral.ai", "huggingface.co",
}

THINK_TANK_HINTS = {
    "rand.org", "cset.georgetown.edu", "brookings.edu", "csis.org", "carnegieendowment.org", "oecd.org",
}

PREFERRED_NEWS_DOMAINS = {
    "reuters.com", "ft.com", "nytimes.com", "bloomberg.com", "wsj.com", "cnbc.com", "axios.com",
    "theatlantic.com", "washingtonpost.com", "economist.com", "tomshardware.com", "digitimes.com",
    "theregister.com", "theverge.com", "semianalysis.com", "politico.com", "govtech.com",
    "cna.asia", "channelnewsasia.com", "cepa.org", "thediplomat.com", "foreignpolicy.com",
    "foreignaffairs.com", "techcrunch.com", "theinformation.com", "nature.com",
}

LOW_SIGNAL_DOMAINS = {
    "marketbeat.com", "tradingview.com", "financialcontent.com", "investing.com", "benzinga.com",
    "pharmaphorum.com", "oilandgas360.com", "pakobserver.net", "travelandtourworld.com",
    "latestnews.az", "moderndiplomacy.eu", "worldoil.com",
}

AI_CORE_TERMS = {
    "ai", "artificial intelligence", "model", "models", "llm", "gpu", "chip", "chips", "semiconductor",
    "compute", "cloud", "data center", "open-weight", "open source", "open-source", "frontier model",
    "qwen", "deepseek", "llama", "mistral", "openai", "anthropic", "meta", "nvidia", "huawei",
}

GEO_TERMS = {
    "china", "beijing", "united states", "u.s.", "washington", "eu", "europe", "brussels",
    "export control", "sanction", "sovereignty", "industrial policy", "security review", "geopolitics",
    "technology rivalry", "biden", "trump", "state council", "ndrc", "cac", "bis", "nist", "ai act",
}

LOW_SIGNAL_PATTERNS = [
    "stock position",
    "holdings in",
    "weekly market commentary",
    "tradingview",
    "web3 tools",
    "monthly users",
    "share price",
    "dividend",
    "analyst rating",
    "earnings preview",
    "increases position in",
    "reduces holdings in",
    "monthly users",
    "buyout of major utility",
    "market commentary",
    "creator tools",
]

HIGH_SIGNAL_PATTERNS = [
    "export control",
    "security review",
    "ai act",
    "state council",
    "ndrc",
    "cac",
    "miit",
    "open-weight",
    "open source",
    "open-source",
    "sovereign wealth",
    "petrodollar",
    "gulf",
    "compute sovereignty",
    "chip ban",
    "frontier model",
]

FOCUS_SYNERGY_TERMS = {
    "petrodollars": ["petrodollar", "petrodollars", "gulf", "sovereign wealth", "oil", "gas", "aramco", "qatar", "uae", "saudi", "abu dhabi", "doha", "riyadh", "energy infrastructure"],
    "manus": ["manus", "meta", "acquisition", "security review", "offshore", "singapore entity"],
    "open-models": ["open-weight", "open source", "open-source", "llama", "qwen", "deepseek", "mistral", "hugging face", "license"],
}


@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str
    published_at: str | None
    source_name: str
    query: str
    provider: str


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "item"


def focus_slug(text: str | None) -> str | None:
    if not text:
        return None
    slug = slugify(text)
    return slug[:60] if slug else None


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    clean = parsed._replace(query="", fragment="")
    return clean.geturl().rstrip("/")


def classify_source(url: str) -> str:
    hostname = urlparse(url).hostname or ""
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in GOVERNMENT_DOMAINS):
        return "government"
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in THINK_TANK_HINTS):
        return "think-tank"
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in INDUSTRY_HINTS):
        return "industry"
    return "mainstream"


def source_quality(url: str) -> int:
    hostname = urlparse(url).hostname or ""
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in LOW_SIGNAL_DOMAINS):
        return -2
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in GOVERNMENT_DOMAINS):
        return 3
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in THINK_TANK_HINTS):
        return 3
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in INDUSTRY_HINTS):
        return 2
    if any(hostname == domain or hostname.endswith(f".{domain}") for domain in PREFERRED_NEWS_DOMAINS):
        return 2
    return 0


def actor_tags(text: str) -> list[str]:
    haystack = text.lower()
    tags: list[str] = []
    if any(word in haystack for word in ["china", "beijing", "huawei", "cac", "miit", "ndrc", "qwen", "deepseek"]):
        tags.append("china")
    if any(word in haystack for word in ["united states", "u.s.", "us ", "washington", "openai", "meta", "white house", "bis", "nist", "nvidia"]):
        tags.append("us")
    if any(word in haystack for word in ["european union", "eu ", "brussels", "europe", "ai act", "asml", "mistral"]):
        tags.append("eu")
    if not tags:
        tags.append("shared")
    return sorted(set(tags))


def topic_tags(text: str) -> list[str]:
    haystack = text.lower()
    mapping = {
        "chips": ["chip", "gpu", "semiconductor", "asml", "tsmc"],
        "compute": ["compute", "supercomputer", "cluster", "exaflop"],
        "cloud": ["cloud", "hyperscaler", "data center"],
        "policy": ["policy", "white paper", "plan"],
        "regulation": ["regulation", "rule", "act", "review", "ban", "security review"],
        "open-models": ["open-weight", "open source", "open-source", "llama", "qwen", "deepseek", "mistral"],
        "safety": ["safety", "alignment", "evaluation"],
        "m-and-a": ["acquisition", "merger", "deal", "buyout"],
        "infrastructure": ["infrastructure", "data center", "power grid", "server farm"],
        "military": ["military", "defense", "deterrence", "pla"],
    }
    tags = [tag for tag, needles in mapping.items() if any(needle in haystack for needle in needles)]
    return tags or ["general-ai"]


def relevance_score(title: str, snippet: str, url: str, focus_terms: list[str] | None = None) -> tuple[int, list[str]]:
    haystack = f"{title} {snippet} {url}".lower()
    reasons: list[str] = []
    score = 0

    ai_hits = sum(1 for term in AI_CORE_TERMS if term in haystack)
    geo_hits = sum(1 for term in GEO_TERMS if term in haystack)

    if ai_hits:
        score += min(ai_hits, 4)
        reasons.append(f"ai:{ai_hits}")
    if geo_hits:
        score += min(geo_hits, 4)
        reasons.append(f"geo:{geo_hits}")

    quality = source_quality(url)
    score += quality
    if quality:
        reasons.append(f"source:{quality}")

    if focus_terms:
        focus_hits = sum(1 for term in focus_terms if term and term in haystack)
        if focus_hits:
            score += focus_hits * 2
            reasons.append(f"focus:{focus_hits}")

        synergy_hits = 0
        for focus_term in focus_terms:
            for key, terms in FOCUS_SYNERGY_TERMS.items():
                if focus_term in key or key in focus_term:
                    synergy_hits += sum(1 for term in terms if term in haystack)
        if synergy_hits:
            score += min(synergy_hits, 4)
            reasons.append(f"synergy:{synergy_hits}")

    if any(pattern in haystack for pattern in LOW_SIGNAL_PATTERNS):
        score -= 3
        reasons.append("low-signal")

    high_signal_hits = sum(1 for pattern in HIGH_SIGNAL_PATTERNS if pattern in haystack)
    if high_signal_hits:
        score += min(high_signal_hits, 3)
        reasons.append(f"high-signal:{high_signal_hits}")

    if "open source" in haystack or "open-source" in haystack or "open-weight" in haystack:
        score += 2
        reasons.append("open-model")

    return score, reasons


def should_accept_result(result: SearchResult, score: int, reasons: list[str], focus_terms: list[str] | None = None) -> tuple[bool, str]:
    hostname = urlparse(result.url).hostname or ""
    has_focus = any(reason.startswith("focus:") or reason.startswith("synergy:") for reason in reasons)
    has_high_signal = any(reason.startswith("high-signal:") for reason in reasons)
    quality = source_quality(result.url)

    if quality < 0 and not has_focus:
        return False, f"low-quality-domain ({hostname})"

    if score < 3 and not has_focus:
        return False, f"low-relevance ({', '.join(reasons)})"

    if quality == 0 and not has_high_signal and not has_focus:
        return False, f"weak-source-without-policy-signal ({hostname})"

    title_lower = result.title.lower()
    if any(pattern in title_lower for pattern in LOW_SIGNAL_PATTERNS) and not has_focus:
        return False, f"low-signal-title ({hostname})"

    return True, "accepted"


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"seen": {}}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"seen": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


async def tavily_search(query: str, days: int, max_results: int) -> list[SearchResult]:
    if not TAVILY_API_KEY:
        return []
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "max_results": max_results,
        "days": days,
        "include_raw_content": True,
        "topic": "news",
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        res = await client.post("https://api.tavily.com/search", json=payload)
        res.raise_for_status()
        data = res.json()
    results: list[SearchResult] = []
    for item in data.get("results", []):
        results.append(
            SearchResult(
                title=item.get("title", "Untitled"),
                url=item.get("url", ""),
                snippet=item.get("raw_content") or item.get("content") or "",
                published_at=item.get("published_date"),
                source_name=item.get("source") or urlparse(item.get("url", "")).hostname or "unknown",
                query=query,
                provider="tavily",
            )
        )
    return results


async def serpapi_search(query: str, days: int, max_results: int) -> list[SearchResult]:
    if not SERPAPI_API_KEY:
        return []
    params = {
        "engine": "google",
        "api_key": SERPAPI_API_KEY,
        "q": query,
        "num": max_results,
        "tbm": "nws",
        "tbs": f"qdr:d{max(days, 1)}",
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        res = await client.get("https://serpapi.com/search.json", params=params)
        res.raise_for_status()
        data = res.json()
    results: list[SearchResult] = []
    for item in data.get("news_results", []) or data.get("organic_results", []):
        results.append(
            SearchResult(
                title=item.get("title", "Untitled"),
                url=item.get("link") or item.get("url") or "",
                snippet=item.get("snippet") or "",
                published_at=item.get("date"),
                source_name=item.get("source") or urlparse(item.get("link", "")).hostname or "unknown",
                query=query,
                provider="serpapi",
            )
        )
    return results


def strip_html(html: str) -> str:
    html = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<style.*?</style>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


async def fetch_article_text(url: str, fallback_text: str = "") -> str:
    try:
        async with httpx.AsyncClient(timeout=45.0, follow_redirects=True, headers={"User-Agent": "Mozilla/5.0"}) as client:
            res = await client.get(url)
            res.raise_for_status()
            content_type = res.headers.get("Content-Type", "")
            if "text/html" in content_type:
                text = strip_html(res.text)
            else:
                text = res.text
            return text[:20000] if text else fallback_text
    except Exception:
        return fallback_text


def target_path(source_class: str, title: str, published_at: str | None, focus_query: str | None = None) -> Path:
    date_prefix = datetime.now().strftime("%Y-%m-%d")
    if published_at:
        match = re.search(r"(\d{4}-\d{2}-\d{2})", published_at)
        if match:
            date_prefix = match.group(1)
    filename = f"{date_prefix}-{slugify(title)[:80]}.md"
    if focus_query:
        root = RAW_FOCUS_ROOT / focus_slug(focus_query)
    else:
        root = RAW_REG_DOCS if source_class == "government" else RAW_ARTICLES
    return root / filename


def render_markdown(result: SearchResult, source_class: str, actors: list[str], topics: list[str], body: str, focus_query: str | None = None) -> str:
    lines = [
        f"# {result.title}",
        "",
        f"> Source: {result.url}",
        f"> Collected: {datetime.now().strftime('%Y-%m-%d')}",
    ]
    if result.published_at:
        lines.append(f"> Published: {result.published_at}")
    lines.extend(
        [
            f"> Source Class: {source_class}",
            f"> Query: {result.query}",
            f"> Search Provider: {result.provider}",
            f"> Focus Query: {focus_query or 'none'}",
            f"> Actor Tags: {', '.join(actors)}",
            f"> Topic Tags: {', '.join(topics)}",
            "",
            body.strip() or result.snippet.strip() or "No extractable body text retrieved.",
            "",
        ]
    )
    return "\n".join(lines)


async def run_news_ingest(days: int, max_per_query: int, topics: list[str] | None = None, focus_query: str | None = None) -> dict:
    topics = topics or list(TOPIC_QUERIES.keys())
    state = load_state()
    seen: dict = state.setdefault("seen", {})
    saved: list[dict] = []
    skipped: list[dict] = []
    failed: list[dict] = []
    focus_terms = [term.strip().lower() for term in re.split(r"[,;/]", focus_query or "") if term.strip()]

    RAW_ARTICLES.mkdir(parents=True, exist_ok=True)
    RAW_REG_DOCS.mkdir(parents=True, exist_ok=True)
    RAW_FOCUS_ROOT.mkdir(parents=True, exist_ok=True)
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

    for topic in topics:
        for query in TOPIC_QUERIES.get(topic, []):
            results = []
            try:
                results.extend(await tavily_search(query, days=days, max_results=max_per_query))
            except Exception as exc:
                failed.append({"query": query, "reason": f"tavily: {exc}"})
            try:
                results.extend(await serpapi_search(query, days=days, max_results=max_per_query))
            except Exception as exc:
                failed.append({"query": query, "reason": f"serpapi: {exc}"})

            deduped: dict[str, SearchResult] = {}
            for result in results:
                if not result.url:
                    continue
                deduped.setdefault(normalize_url(result.url), result)

            for url, result in deduped.items():
                if url in seen:
                    skipped.append({"url": url, "title": result.title, "reason": "already-seen"})
                    continue

                score, reasons = relevance_score(result.title, result.snippet, url, focus_terms=focus_terms)
                accepted, reason = should_accept_result(result, score, reasons, focus_terms=focus_terms)
                if not accepted:
                    skipped.append({"url": url, "title": result.title, "reason": reason})
                    continue

                source_class = classify_source(url)
                tags_text = f"{result.title} {result.snippet} {url}"
                actors = actor_tags(tags_text)
                result_topics = sorted(set(topic_tags(tags_text) + [topic]))
                body = await fetch_article_text(url, fallback_text=result.snippet)
                out_path = target_path(source_class, result.title, result.published_at)
                if out_path.exists():
                    out_path = out_path.with_stem(f"{out_path.stem}-{slugify(urlparse(url).netloc)[:20]}")
                markdown = render_markdown(result, source_class, actors, result_topics, body)
                out_path.write_text(markdown, encoding="utf-8")
                seen[url] = {
                    "title": result.title,
                    "saved_at": datetime.now().isoformat(),
                    "path": str(out_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                }
                saved.append({
                    "url": url,
                    "title": result.title,
                    "path": seen[url]["path"],
                    "source_class": source_class,
                    "actors": actors,
                    "topics": result_topics,
                    "score": score,
                    "reasons": reasons,
                })

    if focus_query:
        for query in [focus_query]:
            results = []
            try:
                results.extend(await tavily_search(query, days=days, max_results=max_per_query))
            except Exception as exc:
                failed.append({"query": query, "reason": f"tavily: {exc}"})
            try:
                results.extend(await serpapi_search(query, days=days, max_results=max_per_query))
            except Exception as exc:
                failed.append({"query": query, "reason": f"serpapi: {exc}"})

            deduped: dict[str, SearchResult] = {}
            for result in results:
                if result.url:
                    deduped.setdefault(normalize_url(result.url), result)

            for url, result in deduped.items():
                if url in seen:
                    skipped.append({"url": url, "title": result.title, "reason": "already-seen"})
                    continue
                score, reasons = relevance_score(result.title, result.snippet, url, focus_terms=focus_terms)
                accepted, reason = should_accept_result(result, score, reasons, focus_terms=focus_terms)
                if not accepted and score < 6:
                    skipped.append({"url": url, "title": result.title, "reason": reason})
                    continue
                source_class = classify_source(url)
                tags_text = f"{result.title} {result.snippet} {url}"
                actors = actor_tags(tags_text)
                result_topics = sorted(set(topic_tags(tags_text) + ["focus-query"]))
                body = await fetch_article_text(url, fallback_text=result.snippet)
                out_path = target_path(source_class, result.title, result.published_at, focus_query=focus_query)
                out_path.parent.mkdir(parents=True, exist_ok=True)
                if out_path.exists():
                    out_path = out_path.with_stem(f"{out_path.stem}-{slugify(urlparse(url).netloc)[:20]}")
                markdown = render_markdown(result, source_class, actors, result_topics, body, focus_query=focus_query)
                out_path.write_text(markdown, encoding="utf-8")
                seen[url] = {
                    "title": result.title,
                    "saved_at": datetime.now().isoformat(),
                    "path": str(out_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                }
                saved.append({
                    "url": url,
                    "title": result.title,
                    "path": seen[url]["path"],
                    "source_class": source_class,
                    "actors": actors,
                    "topics": result_topics,
                    "score": score,
                    "reasons": reasons,
                })

    state["last_run"] = datetime.now().isoformat()
    save_state(state)
    write_report(saved, skipped, failed, days, topics, focus_query)
    return {"saved": saved, "skipped": skipped, "failed": failed}


def write_report(saved: list[dict], skipped: list[dict], failed: list[dict], days: int, topics: list[str], focus_query: str | None) -> None:
    lines = [
        "# News Ingest Report",
        "",
        f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} local",
        f"> Window: last {days} days",
        f"> Topics: {', '.join(topics)}",
        f"> Focus Query: {focus_query or 'none'}",
        "",
        f"## Saved ({len(saved)})",
        "",
    ]
    for item in saved:
        lines.append(f"- `{item['path']}`")
        lines.append(f"  Title: {item['title']}")
        lines.append(f"  Source class: {item['source_class']}")
        lines.append(f"  Actors: {', '.join(item['actors'])}")
        lines.append(f"  Topics: {', '.join(item['topics'])}")
        lines.append(f"  Relevance: {item['score']} ({', '.join(item['reasons'])})")
        lines.append("")
    lines.append(f"## Skipped ({len(skipped)})")
    lines.append("")
    for item in skipped:
        lines.append(f"- {item['title']} ({item['reason']})")
    lines.append("")
    lines.append(f"## Failed ({len(failed)})")
    lines.append("")
    for item in failed:
        lines.append(f"- {item.get('query', item.get('url', 'unknown'))}: {item['reason']}")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

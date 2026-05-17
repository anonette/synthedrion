"""Scheduled session runner for weekly automated sessions."""

import asyncio
import random
from datetime import datetime, timedelta
from typing import Optional

from .models import SessionStartRequest, SessionMessageRequest
from .agent_logic import build_summary, build_wiki_proposals, generate_actor_turn, next_actor
from .wiki_loader import collect_actor_pages, extract_notes, relative_wiki_path
from .llm import generate_openrouter_turn, openrouter_enabled
from .models import SessionState, TranscriptMessage, SessionSummary, MemoOption, WikiProposal
from .database import clear_featured_weekly, get_db, save_session_to_db

# Prompt themes for variety
PROMPT_THEMES = [
    "chip controls and supply chains",
    "AI safety and alignment", 
    "compute sovereignty and cloud dependence",
    "AI labor displacement and social stability",
    "military AI applications and deterrence",
    "AI governance frameworks and standards",
    "data localization and cross-border flows",
    "open source AI vs proprietary models",
    "AGI race dynamics and capability thresholds",
    "AI industrial policy and state subsidies",
]

PROMPT_TEMPLATES = [
    "{actors} debate the implications of {theme} for global AI leadership and strategic advantage.",
    "Breaking: New developments in {theme} shake the global order. How do {actors} respond?",
    "{actors} must negotiate a framework for {theme} while protecting their interests.",
    "As {theme} becomes critical, {actors} balance cooperation and competition.",
    "The question of {theme} divides {actors}. Each must defend their position.",
]


def generate_weekly_prompt() -> str:
    """Generate a fresh prompt for the weekly session."""
    theme = random.choice(PROMPT_THEMES)
    template = random.choice(PROMPT_TEMPLATES)
    
    # Add some variety with current events style
    if random.random() > 0.5:
        recent_event = generate_plausible_event(theme)
        prompt = f"{recent_event} {template}"
    else:
        prompt = template
    
    return prompt.format(
        actors="China, US, and EU",
        theme=theme
    )


def generate_plausible_event(theme: str) -> str:
    """Generate a plausible current event related to the theme."""
    events = {
        "chip controls and supply chains": [
            "A major foundry announces new capacity constraints.",
            "Export control loopholes are discovered and exploited.",
            "A new chip architecture bypasses current restrictions.",
        ],
        "AI safety and alignment": [
            "A frontier lab reports concerning capability jumps.",
            "International safety standards face implementation challenges.",
            "A major AI incident triggers calls for regulation.",
        ],
        "compute sovereignty and cloud dependence": [
            "Critical cloud infrastructure faces sovereignty challenges.",
            "National compute reserves are proposed by multiple nations.",
            "Cross-border compute access becomes politically contentious.",
        ],
        "AI labor displacement and social stability": [
            "AI automation accelerates beyond projections.",
            "Mass retraining programs show mixed results.",
            "Labor unions demand AI deployment restrictions.",
        ],
        "military AI applications and deterrence": [
            "Autonomous systems blur deterrence doctrines.",
            "AI-enabled surveillance reaches new capabilities.",
            "Military AI accidents raise control questions.",
        ],
    }
    
    theme_events = events.get(theme, ["Unexpected developments emerge."])
    return random.choice(theme_events)


async def run_scheduled_session(
    max_duration_seconds: int = 1800,  # 30 minutes
    turn_delay_seconds: int = 30,  # 30 seconds between turns
    min_turns: int = 6,  # At least 2 rounds
    max_turns: int = 18,  # At most 6 rounds
) -> dict:
    """Run a complete automated session."""

    now = datetime.utcnow()
    iso_year, iso_week, iso_weekday = now.isocalendar()
    week_start = (now - timedelta(days=iso_weekday - 1)).date()
    week_key = f"{iso_year}-W{iso_week:02d}"

    # Generate fresh prompt
    prompt = generate_weekly_prompt()
    theme = next((item for item in PROMPT_THEMES if item in prompt), None)
    
    # Start session
    session_state = SessionState(
        session_id=f"auto_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}",
        mode="debate",
        actors=["china", "us", "eu"],
        prompt=prompt,
        loaded_pages={},
        context_notes={},
    )
    
    # Load actor pages
    for actor in session_state.actors:
        pages = collect_actor_pages(actor, include_shared=True)
        session_state.loaded_pages[actor] = [relative_wiki_path(page) for page in pages]
        notes = []
        for page in pages:
            notes.extend(extract_notes(page))
        session_state.context_notes[actor] = notes[:40]
    
    # Run session
    start_time = datetime.utcnow()
    
    while session_state.turn_index < max_turns:
        # Check duration
        elapsed = (datetime.utcnow() - start_time).total_seconds()
        if elapsed > max_duration_seconds and session_state.turn_index >= min_turns:
            break
        
        # Get next actor
        actor, new_index = next_actor(session_state.actors, session_state.next_actor_index)
        
        # Generate turn
        recent_context = [m.model_dump() for m in session_state.transcript[-3:]]
        
        if openrouter_enabled():
            try:
                content = generate_openrouter_turn(
                    actor=actor,
                    actor_label=actor.capitalize() if actor != "us" else "United States",
                    prompt=session_state.prompt,
                    notes=session_state.context_notes.get(actor, []),
                    recent_context=recent_context,
                    mode=session_state.mode,
                )
            except Exception as exc:
                content = generate_actor_turn(
                    actor=actor,
                    mode=session_state.mode,
                    prompt=session_state.prompt,
                    notes=session_state.context_notes.get(actor, []),
                    turn_index=session_state.turn_index,
                    recent_context=recent_context,
                )
        else:
            content = generate_actor_turn(
                actor=actor,
                mode=session_state.mode,
                prompt=session_state.prompt,
                notes=session_state.context_notes.get(actor, []),
                turn_index=session_state.turn_index,
                recent_context=recent_context,
            )
        
        # Add to transcript
        msg = TranscriptMessage(actor=actor, content=content, kind="agent")
        session_state.transcript.append(msg)
        session_state.turn_index += 1
        session_state.next_actor_index = new_index
        
        # Save progress
        with next(get_db()) as db:
            save_session_to_db(
                session_state,
                db,
                metadata={
                    "session_type": "weekly",
                    "week_key": week_key,
                    "week_start": week_start,
                    "is_featured_weekly": False,
                    "title": prompt.split(".", 1)[0].strip(),
                    "theme": theme,
                },
            )
        
        # Delay between turns
        await asyncio.sleep(turn_delay_seconds)
    
    # Generate summary
    summary_data = build_summary(
        session_state.prompt,
        [m.content for m in session_state.transcript],
        session_state.actors,
        session_state.mode
    )
    summary_data["strategic_options"] = [
        MemoOption(**opt) for opt in summary_data["strategic_options"]
    ]
    session_state.summary = SessionSummary(**summary_data)
    
    # Generate wiki proposals
    proposals = build_wiki_proposals(session_state.actors, session_state.prompt)
    session_state.wiki_proposals = [WikiProposal(**prop) for prop in proposals]
    
    # Mark as completed
    session_state.status = "completed"
    
    # Final save
    with next(get_db()) as db:
        clear_featured_weekly(db)
        save_session_to_db(
            session_state,
            db,
            metadata={
                "session_type": "weekly",
                "week_key": week_key,
                "week_start": week_start,
                "is_featured_weekly": True,
                "title": prompt.split(".", 1)[0].strip(),
                "theme": theme,
            },
        )
    
    return {
        "session_id": session_state.session_id,
        "status": "completed",
        "duration_seconds": (datetime.utcnow() - start_time).total_seconds(),
        "turn_count": session_state.turn_index,
        "prompt": prompt,
        "week_key": week_key,
        "summary_headline": session_state.summary.headline if session_state.summary else None,
    }


async def run_test_session() -> dict:
    """Run a short test session for development."""
    return await run_scheduled_session(
        max_duration_seconds=300,  # 5 minutes
        turn_delay_seconds=5,     # 5 seconds
        min_turns=3,              # At least 1 round
        max_turns=6,              # At most 2 rounds
    )

from __future__ import annotations

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


ActorName = Literal["china", "us", "eu"]
SessionMode = Literal["debate", "negotiation", "crisis", "policy-planning", "propaganda-lab"]
InterventionType = Literal["question", "challenge", "redirect", "source", "shock"]
SessionStatus = Literal["running", "completed"]


class SessionStartRequest(BaseModel):
    prompt: str
    actors: list[ActorName]
    mode: SessionMode = "debate"
    include_shared: bool = True
    auto_generate_opening_turn: bool = False


class SessionMessageRequest(BaseModel):
    session_id: str


class InterventionRequest(BaseModel):
    session_id: str
    content: str
    type: InterventionType = "question"


class ShockRequest(BaseModel):
    session_id: str
    title: str
    content: str
    severity: Literal["low", "medium", "high"] = "medium"


class TranscriptMessage(BaseModel):
    actor: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    kind: Literal["agent", "human", "system"] = "agent"
    metadata: dict[str, Any] = Field(default_factory=dict)


class WikiProposal(BaseModel):
    target: str
    reason: str
    content: str


class MemoOption(BaseModel):
    label: str
    detail: str


class SessionSummary(BaseModel):
    headline: str
    context: str
    points_of_agreement: str
    points_of_disagreement: str
    strategic_options: list[MemoOption]
    risks_and_unknowns: str
    recommended_followups: str
    generated_at: datetime = Field(default_factory=datetime.utcnow)


class SessionState(BaseModel):
    session_id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    mode: SessionMode
    actors: list[ActorName]
    prompt: str
    status: SessionStatus = "running"
    turn_index: int = 0
    next_actor_index: int = 0
    transcript: list[TranscriptMessage] = Field(default_factory=list)
    loaded_pages: dict[str, list[str]] = Field(default_factory=dict)
    summary: SessionSummary | None = None
    wiki_proposals: list[WikiProposal] = Field(default_factory=list)
    context_notes: dict[str, list[str]] = Field(default_factory=dict)

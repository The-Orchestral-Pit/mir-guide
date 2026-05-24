"""Pydantic v2 data model for MIR Guide resources."""

from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl, model_validator

_MARKETING_WORDS = {
    "leading",
    "best",
    "world-class",
    "cutting-edge",
    "pioneering",
    "groundbreaking",
}


class SourceType(StrEnum):
    ACADEMIC = "academic"
    INDUSTRY = "industry"
    COMMUNITY = "community"
    MEDIA = "media"


class Region(StrEnum):
    EUROPE = "europe"
    NORTH_AMERICA = "north-america"
    ASIA_PACIFIC = "asia-pacific"
    GLOBAL = "global"


class Topic(StrEnum):
    GENERAL_MIR = "general-mir"
    GENERATION = "generation"
    SEPARATION = "separation"
    RECOMMENDATION = "recommendation"
    TRANSCRIPTION = "transcription"
    SYNTHESIS = "synthesis"
    ANALYSIS = "analysis"
    PERFORMANCE = "performance"


class EventType(StrEnum):
    MEETUP = "meetup"
    CONFERENCE = "conference"
    FESTIVAL = "festival"
    HACKATHON = "hackathon"


class PublicationFormat(StrEnum):
    BLOG = "blog"
    NEWSLETTER = "newsletter"
    SUBSTACK = "substack"


class Recurrence(StrEnum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    ANNUAL = "annual"
    AD_HOC = "ad-hoc"


class Resource(BaseModel):
    """A single entry in the MIR Guide catalog."""

    name: str
    url: HttpUrl
    description: str = Field(..., min_length=10, max_length=400)
    source_type: SourceType
    added: date
    verified: date

    region: Region | None = None
    topics: list[Topic] = []
    people: list[str] = []
    institution: str | None = None
    event_type: EventType | None = None
    recurrence: Recurrence | None = None
    location: str | None = None
    pub_format: PublicationFormat | None = None

    @model_validator(mode="after")
    def warn_marketing_language(self) -> "Resource":
        """Warn (but do not reject) descriptions containing marketing superlatives."""
        words = set(self.description.lower().split())
        found = words & _MARKETING_WORDS
        if found:
            flagged = ", ".join(sorted(found))
            print(f"WARNING [{self.name}]: description contains marketing word(s): {flagged}")
        return self

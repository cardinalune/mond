from app.models.identifiers import Identifiers
from dataclasses import dataclass, field

@dataclass
class Book:
    
    title: str
    identifiers: Identifiers
    full_title: str | None = None
    authors: list[str] = field(default_factory=list)
    publish_date: str | None = None
    publishers: list[str] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)
    pages: int | str | None = None
    series: list[str] = field(default_factory=list)
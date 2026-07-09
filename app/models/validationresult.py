from dataclasses import dataclass, field

@dataclass
class ValidationResult:

    match : bool
    confidence : int
    reasons : list[str] = field(default_factory=list)
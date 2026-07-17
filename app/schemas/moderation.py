from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.database.models.submission import SubmissionStatus

class PendingSubmissionResponse(BaseModel):

    id: UUID

    title: str

    validation_score: float

    status: SubmissionStatus

    submitted_at: datetime



class SubmissionDetailResponse(BaseModel):

    id: UUID

    md5: str

    olid: str

    validation_score: float

    is_match: bool

    status: SubmissionStatus

    submitted_at: datetime

    reviewed_at: datetime | None

    anna_snapshot: dict

    ol_snapshot: dict
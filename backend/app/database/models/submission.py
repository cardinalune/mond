from uuid import UUID , uuid4
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from datetime import UTC, datetime
from enum import Enum


from sqlalchemy import (
    Boolean,
    DateTime,
    Float,
    ForeignKey,
    String,
    Enum as SQLEnum,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.database.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.database.models.user import User

class SubmissionStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Submission(Base):

    __tablename__ = "submissions"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )
    user: Mapped["User"] = relationship(
        back_populates="submissions",
        foreign_keys=[user_id]
    )

    moderator_id: Mapped[UUID | None] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=True
    )
    moderator: Mapped["User | None"] = relationship(
        back_populates="reviewed_submissions",
        foreign_keys=[moderator_id]
    )

    md5: Mapped[str] = mapped_column(
        String(32),
        nullable=False
    )

    olid: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    anna_snapshot: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    ol_snapshot: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False
    )

    validation_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    is_match: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    status: Mapped[SubmissionStatus] = mapped_column(
        SQLEnum(SubmissionStatus, name="submission_status"),
        default=SubmissionStatus.PENDING,
        nullable=False
    )

    submitted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

   
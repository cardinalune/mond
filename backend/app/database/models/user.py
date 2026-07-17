
from datetime import UTC, datetime
from enum import Enum
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy import Enum as SQLEnum

from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.database.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.database.models.submission import Submission


class UserRole(str, Enum):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"



class User(Base):

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
    )

    username: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="user_role"),
        default=UserRole.USER,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

    submissions: Mapped[list["Submission"]] = relationship(
        back_populates="user",
        foreign_keys="Submission.user_id"
    )

    reviewed_submissions: Mapped[list["Submission"]] = relationship(
        back_populates="moderator",
        foreign_keys="Submission.moderator_id"
    )

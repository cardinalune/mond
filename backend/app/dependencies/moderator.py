from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.repositories.submission import SubmissionRepository
from app.services.moderator import ModeratorService


def get_moderator_service(
    db: Session = Depends(get_db),
) -> ModeratorService:
    submission_repository = SubmissionRepository(db)

    return ModeratorService(
        submission_repository=submission_repository,
    )
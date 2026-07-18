from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.repositories.submission import SubmissionRepository

from app.services.anna import AnnaService
from app.services.openlibrary import OpenLibraryService
from app.services.validator import Validator
from app.services.moderator import ModeratorService
from app.services.export import ExportService


def get_submission_repository(
    db: Session = Depends(get_db),
) -> SubmissionRepository:
    return SubmissionRepository(db)


def get_anna_service() -> AnnaService:
    return AnnaService()


def get_openlibrary_service() -> OpenLibraryService:
    return OpenLibraryService()


def get_validator() -> Validator:
    return Validator()


def get_moderator_service(
    submission_repository: SubmissionRepository = Depends(
        get_submission_repository
    ),
) -> ModeratorService:
    return ModeratorService(
        submission_repository=submission_repository,
    )


def get_export_service(
    submission_repository: SubmissionRepository = Depends(
        get_submission_repository
    ),
) -> ExportService:
    return ExportService(submission_repository)
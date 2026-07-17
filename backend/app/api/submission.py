from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.anna import AnnaService
from app.services.openlibrary import OpenLibraryService
from app.services.validator import Validator
from app.schemas.submit import SubmitRequest
from app.models.validationresult import ValidationResult
from app.database.database import get_db
from app.database.repositories.submission import SubmissionRepository
from dataclasses import asdict
from app.database.models.user import User
from app.utils.security import get_current_user , require_admin , require_moderator



router = APIRouter()

anna_service = AnnaService()
ol_service = OpenLibraryService()
validator = Validator()


@router.post("/submit")
def submit(
    request: SubmitRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):

    ol_book = ol_service.get_book(request.olid)
    anna_book = anna_service.get_book(request.md5)

    result = validator.validate(ol_book, anna_book)

    submission_repo = SubmissionRepository(db)

    submission = submission_repo.create_submission(
        user_id=current_user.id,
        md5=request.md5,
        olid=request.olid,
        anna_snapshot=asdict(anna_book),
        ol_snapshot=asdict(ol_book),
        validation_score=result.confidence,
        is_match=result.match,
    )

    return {
        "submission_id": str(submission.id),
        "match": result.match,
        "confidence": result.confidence,
        "reasons": result.reasons,
    }

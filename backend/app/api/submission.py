from dataclasses import asdict
from app.models.book import Book

from fastapi import APIRouter, Depends

from app.schemas.submit import SubmitRequest , ValidationResponse , SubmitMappingResponse , SubmitMappingRequest
from app.database.models.user import User
from app.database.repositories.submission import SubmissionRepository

from app.services.anna import AnnaService
from app.services.openlibrary import OpenLibraryService
from app.services.validator import Validator

from app.dependencies.services import (
    get_anna_service,
    get_openlibrary_service,
    get_submission_repository,
    get_validator,
)

from app.utils.security import get_current_user


router = APIRouter()

@router.post(
    "/validate",
    response_model=ValidationResponse,
)
def validate(
    request: SubmitRequest,
    current_user: User = Depends(get_current_user),
    anna_service: AnnaService = Depends(get_anna_service),
    ol_service: OpenLibraryService = Depends(get_openlibrary_service),
    validator: Validator = Depends(get_validator),
):
    ol_book = ol_service.get_book(request.olid)
    anna_book = anna_service.get_book(request.md5)

    result = validator.validate(
        ol_book,
        anna_book,
    )

    return {
        "match": result.match,
        "confidence": result.confidence,
        "reasons": result.reasons,
        "anna_record": asdict(anna_book),
        "openlibrary_record": asdict(ol_book),
    }

@router.post(
    "/submit",
    response_model=SubmitMappingResponse,
)
def submit(
    request: SubmitMappingRequest,
    current_user: User = Depends(get_current_user),
    submission_repo: SubmissionRepository = Depends(
        get_submission_repository,
    ),
):

    submission = submission_repo.create_submission(
        user_id=current_user.id,
        md5=request.md5,
        olid=request.olid,
        anna_snapshot=request.anna_record,
        ol_snapshot=request.openlibrary_record,
        validation_score=request.confidence,
        is_match=request.match,
    )

    return {
        "submission_id": str(submission.id),
        "status": submission.status,
    }
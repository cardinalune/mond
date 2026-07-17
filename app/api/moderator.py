from fastapi import APIRouter, Depends , Query
from sqlalchemy.orm import Session
from uuid import UUID
from app.database.models.user import User
from app.dependencies.moderator import get_moderator_service
from app.utils.security import require_moderator
from app.services.moderator import ModeratorService
from app.schemas.moderation import PendingSubmissionResponse , SubmissionDetailResponse

router = APIRouter(
    prefix="/moderation",
    tags=["Moderation"],
)

@router.get("/pending" , response_model=list[PendingSubmissionResponse],)
def pending(
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    service: ModeratorService = Depends(get_moderator_service),
    current_user: User = Depends(require_moderator),
):

    return service.list_pending(
        limit=limit,
        offset=offset,
    )

@router.get(
    "/submissions/{submission_id}",
    response_model=SubmissionDetailResponse,
)
def get_submission(
    submission_id: UUID,
    service: ModeratorService = Depends(get_moderator_service),
    current_user: User = Depends(require_moderator),
):
    return service.get_submission(submission_id)


@router.post(
    "/submissions/{submission_id}/approve",
    response_model=SubmissionDetailResponse,
)
def approve_submission(
    submission_id: UUID,
    service: ModeratorService = Depends(get_moderator_service),
    current_user: User = Depends(require_moderator),
):
    service.approve_submission(
        submission_id=submission_id,
        moderator=current_user,
    )

    return service.get_submission(submission_id)


@router.post(
    "/submissions/{submission_id}/reject",
    response_model=SubmissionDetailResponse,
)
def reject_submission(
    submission_id: UUID,
    service: ModeratorService = Depends(get_moderator_service),
    current_user: User = Depends(require_moderator),
):
    service.reject_submission(
        submission_id=submission_id,
        moderator=current_user,
    )

    return service.get_submission(submission_id)
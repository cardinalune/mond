from uuid import UUID
from datetime import UTC, datetime

from app.database.models.submission import Submission , SubmissionStatus
from app.database.repositories.submission import SubmissionRepository
from app.database.models.user import User
from app.exceptions.submission import SubmissionAlreadyReviewedError , SubmissionNotFoundError
from app.schemas.moderation import PendingSubmissionResponse , SubmissionDetailResponse


class ModeratorService:

    def __init__(
        self,
        submission_repository: SubmissionRepository,
    ):
        self.submission_repository = submission_repository



    def approve_submission(
        self,
        submission_id: UUID,
        moderator: User,
    ) -> Submission:

        submission = self.submission_repository.get_by_id(submission_id)

        if submission is None:
            raise SubmissionNotFoundError()


        if submission.status != SubmissionStatus.PENDING:
            raise SubmissionAlreadyReviewedError()

        submission.status = SubmissionStatus.APPROVED
        submission.moderator_id = moderator.id
        submission.reviewed_at = datetime.now(UTC)

        return self.submission_repository.save(submission)



    def reject_submission(
        self,
        submission_id: UUID,
        moderator: User,
    ) -> Submission:

        submission = self.submission_repository.get_by_id(submission_id)

        if submission is None:
            raise SubmissionNotFoundError()


        if submission.status != SubmissionStatus.PENDING:
            raise SubmissionAlreadyReviewedError()

        submission.status = SubmissionStatus.REJECTED
        submission.moderator_id = moderator.id
        submission.reviewed_at = datetime.now(UTC)

        return self.submission_repository.save(submission)


    def list_pending(
        self,
        limit: int,
        offset: int,
    ) -> list[PendingSubmissionResponse]:

        submissions = self.submission_repository.list_by_status(
            status=SubmissionStatus.PENDING,
            limit=limit,
            offset=offset,
        )

        responses: list[PendingSubmissionResponse] = []

        for submission in submissions:

            title = submission.anna_snapshot.get(
                "title",
                "Unknown Title",
            )

            responses.append(
                PendingSubmissionResponse(
                    id=submission.id,
                    title=title,
                    validation_score=submission.validation_score,
                    status=submission.status,
                    submitted_at=submission.submitted_at,
                )
            )

        return responses


    def get_submission(
        self,
        submission_id: UUID,
    ) -> SubmissionDetailResponse:
        

        submission = self.submission_repository.get_by_id(submission_id)

        if submission is None:
            raise SubmissionNotFoundError()


        return SubmissionDetailResponse(
        id=submission.id,
        md5=submission.md5,
        olid=submission.olid,
        validation_score=submission.validation_score,
        is_match=submission.is_match,
        status=submission.status,
        submitted_at=submission.submitted_at,
        reviewed_at=submission.reviewed_at,
        anna_snapshot=submission.anna_snapshot,
        ol_snapshot=submission.ol_snapshot,
    )
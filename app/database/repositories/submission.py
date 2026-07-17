from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.database.models.submission import Submission, SubmissionStatus


class SubmissionRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_submission(
        self,
        user_id: UUID,
        md5: str,
        olid: str,
        anna_snapshot: dict,
        ol_snapshot: dict,
        validation_score: float,
        is_match: bool,
    ) -> Submission:

        submission = Submission(
            user_id=user_id,
            md5=md5,
            olid=olid,
            anna_snapshot=anna_snapshot,
            ol_snapshot=ol_snapshot,
            validation_score=validation_score,
            is_match=is_match,
        )

        self.db.add(submission)

        try:
            self.db.commit()
            self.db.refresh(submission)
            return submission

        except SQLAlchemyError:
            self.db.rollback()
        raise

   

    def get_by_id(
        self,
        submission_id: UUID,
    ) -> Submission | None:

        statement = select(Submission).where(
            Submission.id == submission_id
        )

        result = self.db.execute(statement)

        return result.scalar_one_or_none()



    def list_by_status(
        self,
        status: SubmissionStatus,
        limit:int | None=None,
        offset:int =0,
    ) ->list[Submission]:

        statement = (
            select(Submission)
            .where(Submission.status == status)
            .order_by(Submission.submitted_at.asc())
            
        )
        if limit is not None:
            statement = statement.limit(limit)

        statement = statement.offset(offset)

        result = self.db.execute(statement)
        return result.scalars().all()


    def save(
        self,
        submission: Submission,
    ) -> Submission:

        self.db.add(submission)

        try:
            self.db.commit()
            self.db.refresh(submission)
            return submission

        except SQLAlchemyError:
            self.db.rollback()
            raise

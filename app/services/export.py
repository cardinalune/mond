from app.database.repositories.submission import SubmissionRepository
from app.database.models.submission import SubmissionStatus

class ExportService:

    def __init__(
        self,
        submission_repository: SubmissionRepository,
    ):
        self.submission_repository = submission_repository


    def export_mappings(self) -> list[tuple[str, str]]:

        submissions = self.submission_repository.list_by_status(
            status=SubmissionStatus.APPROVED,
            limit=None,
            offset=0,
        )

        return [
            (submission.md5, submission.olid)
            for submission in submissions
        ]
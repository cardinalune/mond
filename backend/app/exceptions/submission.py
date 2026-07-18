class SubmissionNotFoundError(Exception):
    def __init__(self, message: str = "Submission not found"):
        super().__init__(message)


class SubmissionAlreadyReviewedError(Exception):
    def __init__(
        self,
        message: str = "Submission has already been reviewed",
    ):
        super().__init__(message)
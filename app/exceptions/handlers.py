from fastapi.responses import JSONResponse
from fastapi import status , Request


from app.exceptions.service import (ExternalServiceError , InternalServiceError,)
from app.exceptions.book import BookNotFoundError
from app.exceptions.authentication import (
    UsernameAlreadyExistsError,
    EmailAlreadyExistsError,
    InvalidCredentialsError,
    EmailNotVerifiedError,
    InvalidTokenError,
    AuthenticationRequiredError,
    )
from app.exceptions.authorization import PermissionDeniedError
from app.exceptions.user import UserNotFoundError
from app.exceptions.supabase import SupabaseError
from app.exceptions.submission import SubmissionAlreadyReviewedError , SubmissionNotFoundError


def book_not_found_handler(request : Request ,exc : BookNotFoundError,):

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": str(exc)
        }
    )


def external_service_handler(request : Request, exc : ExternalServiceError):

     return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "detail": str(exc)
        }
    )


def internal_service_handler(request : Request , exc : InternalServiceError):

    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = {
            "detail" : str(exc)
        }
    )


def username_already_exists_handler(request : Request,exc : UsernameAlreadyExistsError):

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": str(exc)
        }
    )


def email_already_exists_handler(request : Request , exc : EmailAlreadyExistsError):

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": str(exc)
        }
    )


def invalid_credentials_handler(request : Request , exc : InvalidCredentialsError):
     return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail": str(exc)
        }
    )


def email_not_verified_handler(request : Request , exc : EmailNotVerifiedError):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "detail": str(exc)
        }
    )


def invalid_token_handler(request : Request , exc : InvalidTokenError ):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail": str(exc)
        }
    )


def authentication_required_handler(request : Request , exc : AuthenticationRequiredError ):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "detail": str(exc)
        }
    )


def permission_denied_handler(request : Request , exc : PermissionDeniedError ):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "detail": str(exc)
        }
    )


def user_not_found_handler(request : Request , exc : UserNotFoundError ):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": str(exc)
        }
    )

    
def supabase_error_handler(request : Request , exc : SupabaseError):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "detail": str(exc)
        }
    )


def submission_not_found_handler(request : Request , exc : SubmissionNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": str(exc)
        }
    )



def submission_already_reviewed_handler(request : Request , exc : SubmissionAlreadyReviewedError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        content={
            "detail": str(exc)
        }
    )

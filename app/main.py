from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.submission import router as submit_router
from app.api.auth import router as auth_router
from app.exceptions.book import BookNotFoundError
from app.exceptions.service import ExternalServiceError , InternalServiceError
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

from app.exceptions.handlers import (
    book_not_found_handler,
    external_service_handler,
    username_already_exists_handler,
    email_already_exists_handler,
    invalid_credentials_handler,
    email_not_verified_handler,
    invalid_token_handler,
    authentication_required_handler,
    permission_denied_handler,
    user_not_found_handler,
    supabase_error_handler,
    internal_service_handler,
)



app = FastAPI()

app.add_exception_handler(
    BookNotFoundError,
    book_not_found_handler
)

app.add_exception_handler(
    ExternalServiceError,
    external_service_handler
)

app.add_exception_handler(
    InternalServiceError,
    internal_service_handler
)

app.add_exception_handler(
    UsernameAlreadyExistsError,
    username_already_exists_handler
)

app.add_exception_handler(
    EmailAlreadyExistsError,
    email_already_exists_handler
)

app.add_exception_handler(
    InvalidCredentialsError,
    invalid_credentials_handler
)

app.add_exception_handler(
    EmailNotVerifiedError,
    email_not_verified_handler
)

app.add_exception_handler(
    InvalidTokenError,
    invalid_token_handler
)

app.add_exception_handler(
    AuthenticationRequiredError,
    authentication_required_handler
)

app.add_exception_handler(
    PermissionDeniedError,
    permission_denied_handler
)

app.add_exception_handler(
    UserNotFoundError,
    user_not_found_handler
)

app.add_exception_handler(
    SupabaseError,
    supabase_error_handler
)



app.include_router(health_router)
app.include_router(submit_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return{
        "message":"Welcome to Mond"
    }




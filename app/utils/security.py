from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.repositories.userrepository import UserRepository
from app.database.models.user import User
from app.exceptions.authorization import PermissionDeniedError
from app.utils.supabase import supabase
from app.exceptions.authentication import InvalidTokenError , AuthenticationRequiredError 
from app.exceptions.user import UserNotFoundError
from typing import Optional


security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db),
) -> User:

    if credentials is None:
        raise AuthenticationRequiredError(
            "Authentication required."
        )

    if credentials.scheme.lower() != "bearer":
        raise InvalidTokenError(
            "Invalid authentication scheme."
        )

    token = credentials.credentials

    try:
        response = supabase.auth.get_user(token)
    except Exception as e:
        raise InvalidTokenError(
            "Invalid or expired token."
        ) from e

    if response.user is None:
        raise InvalidTokenError(
            "Invalid or expired token."
        )

    user_repo = UserRepository(db)

    user = user_repo.get_by_id(
        UUID(response.user.id)
    )

    if user is None:
        raise UserNotFoundError(
            "User not found."
        )

    if not user.is_active:
        raise PermissionDeniedError(
            "Your account has been disabled."
        )

    return user
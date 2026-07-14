from uuid import UUID

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.repositories.user import UserRepository
from app.database.models.user import User
from app.exceptions.authorization import PermissionDeniedError
from app.utils.supabase import supabase
from app.exceptions.authentication import InvalidTokenError , AuthenticationRequiredError 
from app.exceptions.user import UserNotFoundError
from typing import Optional
from app.database.models.user import UserRole


security = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    """
    Authenticate the current user using a Supabase access token.

    Returns:
        User: The authenticated Mond user.

    Raises:
        AuthenticationRequiredError
        InvalidTokenError
        UserNotFoundError
        PermissionDeniedError
    """

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


def require_moderator(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Require the authenticated user to be a moderator or admin.
    """

    if current_user.role not in (
        UserRole.MODERATOR,
        UserRole.ADMIN,
    ):
        raise PermissionDeniedError(
            "Moderator privileges required."
        )

    return current_user


def require_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Require the authenticated user to be an administrator.
    """

    if current_user.role != UserRole.ADMIN:
        raise PermissionDeniedError(
            "Administrator privileges required."
        )

    return current_user
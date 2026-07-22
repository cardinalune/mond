from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils.security import get_current_user
from app.database.models.user import User
from app.database.database import get_db
from app.schemas.auth import LoginResponse, SignupRequest , SignupResponse , LoginRequest , CurrentUserResponse
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup" ,  response_model=SignupResponse,)
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    return service.signup(request)


@router.post("/login" , response_model= LoginResponse)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    return service.login(request)



@router.get(
    "/me",
    response_model=CurrentUserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return CurrentUserResponse(
        id=str(current_user.id),
        username=current_user.username,
        email=current_user.email,
        role=current_user.role.value,
    )
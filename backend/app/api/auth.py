from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.database import get_db
from app.schemas.auth import LoginResponse, SignupRequest , SignupResponse , LoginRequest
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
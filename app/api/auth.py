from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import SignupRequest
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/signup")
def signup(
    request: SignupRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    return service.signup(request)
from sqlalchemy.orm import Session

from app.exceptions.authenctication import UsernameAlreadyExistsError
from app.exceptions.supabase import SupabaseError
from app.schemas.auth import SignupRequest
from app.database.repositories.userrepository import UserRepository
from app.utils.supabase import supabase

class AuthService:

    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)


    def signup(self, request: SignupRequest):

        existing = self.user_repo.get_by_username(request.username)

        if existing:
            raise UsernameAlreadyExistsError(
                f"{request.username} already exists"
            )

        try:
            response = supabase.auth.sign_up(
                {
                    "email": request.email,     
                    "password": request.password,
                }
            )
        except Exception as e:
            raise SupabaseError(
            " Failed to communicate with Supabase."
            ) from e


        if response.user is None:
            raise SupabaseError("Failed to create account")




        user = self.user_repo.create_user(
            user_id=response.user.id,
            username=request.username,
            email=request.email,
        )

        return {
            "message": (
                "Account created successfully. "
                "Please check your email to verify your account."
            ),
            "user_id": str(user.id),
        }
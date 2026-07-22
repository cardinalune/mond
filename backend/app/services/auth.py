from sqlalchemy.orm import Session
from app.exceptions.authentication import UsernameAlreadyExistsError , InvalidCredentialsError , EmailNotVerifiedError , EmailAlreadyExistsError
from app.exceptions.supabase import SupabaseError
from app.exceptions.service import InternalServiceError
from app.schemas.auth import SignupRequest , LoginRequest , SignupResponse , LoginResponse
from app.database.repositories.user import UserRepository
from app.utils.supabase import supabase
from fastapi import HTTPException

class AuthService:

    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)


    def signup(self, request: SignupRequest)-> SignupResponse:

        existingUser = self.user_repo.get_by_username(request.username)
        existingEmail = self.user_repo.get_by_email(request.email)

        if existingUser:
            raise UsernameAlreadyExistsError(
                f"{request.username} already exists"
            )

        if existingEmail:
            raise EmailAlreadyExistsError(
                "Email already exists"
            )

        try:
            response = supabase.auth.sign_up(
                {
                    "email": request.email,     
                    "password": request.password,
                }
            )
        except Exception as e:
            print("Supabase error:", e)
            raise HTTPException(
                status_code=503,
                detail=str(e)
            )


        if response.user is None:
            raise SupabaseError("Failed to create account")




        user = self.user_repo.create_user(
            user_id=response.user.id,
            username=request.username,
            email=request.email,
        )

        return SignupResponse (
            message=("Account created successfully. "
                "Please check your email to verify your account."),
            user_id=str(user.id),
        )


    def login(self, request: LoginRequest) ->LoginResponse:

        try:
            response = supabase.auth.sign_in_with_password({
        "email": request.email,
        "password": request.password,
        })
        except Exception as e:
            message = str(e).lower()

            
       
            if "email not confirmed" in message:
                raise EmailNotVerifiedError(
                    "Please verify your email before logging in."
                ) from e

            if "invalid login credentials" in message:
                raise InvalidCredentialsError(
                    "Invalid email or password."
                ) from e

            raise SupabaseError(
                "Failed to communicate with Supabase."
            ) from e
            
        user = self.user_repo.get_by_email(request.email)

        return LoginResponse(
            access_token=response.session.access_token,
            refresh_token=response.session.refresh_token,
            expires_in=response.session.expires_in,
            token_type="Bearer",
            role=user.role.value,
        )


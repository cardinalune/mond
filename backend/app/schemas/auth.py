from pydantic import BaseModel, EmailStr, Field


class SignupRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class SignupResponse(BaseModel):
    message: str
    user_id: str




class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str = "Bearer"

    role: str


class CurrentUserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    role: str
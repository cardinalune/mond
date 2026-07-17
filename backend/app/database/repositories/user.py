from sqlalchemy import select
from sqlalchemy.orm import Session
from uuid import UUID
from sqlalchemy.exc import SQLAlchemyError


from app.database.models.user import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(
        self,
        user_id: UUID,
        username: str,
        email: str,
        
    ) -> User:

        user = User(
            id=user_id,
            username=username,
            email=email,
        )

        self.db.add(user)
        try:
            self.db.commit()
            self.db.refresh(user)  # Fixed: Moved inside or after successful commit
            return user            # Fixed: Properly returns the created user
        except SQLAlchemyError:
            self.db.rollback()
            raise   
        


    def get_by_id(self, user_id: UUID) -> User | None:
        statement = select(User).where(User.id == user_id)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()

        
    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()


    def get_by_username(self , username : str) -> User | None:
        statement = select(User).where(User.username == username)

        result = self.db.execute(statement)

        return result.scalar_one_or_none()



    
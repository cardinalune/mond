from app.database.database import Base, engine



from app.database.models.user import User
from app.database.models.submission import Submission



Base.metadata.create_all(bind=engine)
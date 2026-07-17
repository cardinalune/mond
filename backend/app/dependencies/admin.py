from app.database.repositories.submission import SubmissionRepository
from sqlalchemy.orm import Session
from fastapi import  Depends
from app.services.export import ExportService
from app.database.database import get_db

def get_export_service(
    db: Session = Depends(get_db),
) -> ExportService:

    repository = SubmissionRepository(db)

    return ExportService(repository)
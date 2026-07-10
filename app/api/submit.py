from fastapi import APIRouter
from app.services.annaservice import AnnaService
from app.services.openlibraryservice import OpenLibraryService
from app.services.validator import Validator
from app.schemas.submit import SubmitRequest
from app.models.validationresult import ValidationResult

router = APIRouter()

anna_service = AnnaService()
ol_service = OpenLibraryService()
validator = Validator()


@router.post("/submit")
def submit(request : SubmitRequest):
    
    ol_book = ol_service.get_book(request.olid)
    anna_book = anna_service.get_book(request.md5)

    result =validator.validate(ol_book ,anna_book )

    
    return{
        "match" : result.match,
        "confidence" : result.confidence,
        "list" : result.reasons
    }
     

    
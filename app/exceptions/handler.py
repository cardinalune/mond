from app.exceptions.serviceexceptions import ExternalServiceError
from app.exceptions.bookexceptions import BookNotFoundError
from fastapi.responses import JSONResponse
from fastapi import status , Request

def book_not_found_handler(
    request : Request ,
    exc : BookNotFoundError,
    ):

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": str(exc)
        }
    )


def external_service_handler(
    request : Request, 
    exc : ExternalServiceError):

     return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "detail": str(exc)
        }
    )
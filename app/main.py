from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.submit import router as submit_router
from app.exceptions.bookexceptions import BookNotFoundError
from app.exceptions.serviceexceptions import ExternalServiceError
from app.exceptions.handler import (
    book_not_found_handler,
    external_service_handler,
)



app = FastAPI()

app.add_exception_handler(
    BookNotFoundError,
    book_not_found_handler
)

app.add_exception_handler(
    ExternalServiceError,
    external_service_handler
)

app.include_router(health_router)
app.include_router(submit_router)


@app.get("/")
def root():
    return{
        "message":"Welcome to Mond"
    }




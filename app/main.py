from fastapi import FastAPI
from app.schemas.submit import SubmitRequest
from app.api.health import router as health_router
from app.api.submit import router as submit_router



app = FastAPI()

app.include_router(health_router)
app.include_router(submit_router)


@app.get("/")
def root():
    return{
        "message":"mond here"
    }


@app.get("/books/{olid}")
def booklookup(olid):
    return{
        "message": "Looking up book",
        "olid": "OL123M"
    }     


@app.get("/books")
def get_books(page:int=1 , limit:int=10):
    return{"page":page , "limit":limit}  



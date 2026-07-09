from pydantic import BaseModel

class SubmitRequest(BaseModel):
    md5:str
    olid:str
    
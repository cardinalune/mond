from pydantic import BaseModel, field_validator
from datetime import datetime

class SubmitRequest(BaseModel):
    md5:str
    olid:str
    

    @field_validator("md5")
    def validate_md5(cls, value):
        
        if len(value) != 32:
            raise ValueError("MD5 must be exactly 32 characters.")

        try:
            int(value, 16)
        except ValueError:
            raise ValueError("MD5 must contain only hexadecimal characters.")

        return value.lower()



            
    @field_validator("olid")
    def validate_olid(cls, value):
        OLID = value.upper()

        if OLID.startswith("OL") and OLID.endswith("M") and OLID[2:-1].isdigit():
            return OLID
        else:
            raise ValueError("OLID must start with OL and end with M wiith numbers in between")
        

class ValidationResponse(BaseModel):
    match: bool
    confidence: float
    reasons: list[str]

    anna_record: dict
    openlibrary_record: dict


class SubmitMappingRequest(SubmitRequest):
    pass
    

class SubmitMappingResponse(BaseModel):
    submission_id: str
    status: str


class SubmissionHistoryItem(BaseModel):
    id: str
    md5: str
    olid: str

    status: str

    validation_score: float

    submitted_at: datetime

    title: str
    
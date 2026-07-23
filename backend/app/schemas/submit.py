from pydantic import BaseModel, field_validator

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


class SubmitMappingRequest(BaseModel):
    md5: str
    olid: str
    anna_record: dict
    openlibrary_record: dict
    confidence: float
    match: bool

class SubmitMappingResponse(BaseModel):
    submission_id: str
    status: str
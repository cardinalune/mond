from dataclasses import dataclass, field

@dataclass
class Mapping:
    md5 : str
    olid : str
    status : str = "pending"
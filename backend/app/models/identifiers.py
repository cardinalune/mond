from dataclasses import dataclass, field

@dataclass
class Identifiers:

    olwid : str | None = None
    oleid : str | None = None
    md5 :  str | None = None 
    isbn_13: list[str] = field(default_factory=list)
    isbn_10: list[str] = field(default_factory=list)
    oclc: list[str] = field(default_factory=list)
    goodreads: list[str] = field(default_factory=list)
    amazon: list[str] = field(default_factory=list)
    storygraph: list[str] = field(default_factory=list)
    abebooks: list[str] = field(default_factory=list)
    alibris_id: list[str] = field(default_factory=list)
    better_world_books: list[str]= field(default_factory=list)
     
   
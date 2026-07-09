from app.services.openlibraryservice import OpenLibraryService
from app.services.annaservice import AnnaService
from app.services.validator import Validator

ol = OpenLibraryService()
anna = AnnaService()
validator = Validator()

# Same book from both sources
openlibrary_book = ol.get_book(olid="OL38446297M")
anna_book = anna.get_book("26c15681e554b48e2a71b751c50cc7c0")

result = validator.validate(anna_book, openlibrary_book)

print(result)

"""
OL26775548M , 1feaa5e0a8fb813f87163b035456cca6 : Harry Potter and the Philosopher's Stone(both same)
ValidationResult(match=True, confidence=100, reasons=['ISBN-13 matched', 'ISBN-10 matched', 'Title matched (100.0%)', 'Author matched (100.0%)'])

OL61090737M , 1feaa5e0a8fb813f87163b035456cca6 : edition of philospher stone , eng
ValidationResult(match=False, confidence=0, reasons=[])

OL59004869M(1998) , 1feaa5e0a8fb813f87163b035456cca6(2018) : same book
ValidationResult(match=False, confidence=35, reasons=['Title matched (100.0%)', 'Author matched (100.0%)'])

OL38446297M , 26c15681e554b48e2a71b751c50cc7c0 : Twisted Lies (Twisted, 4)A. H, Ana Huang
ValidationResult(match=True, confidence=100, reasons=['OLEID matched'])

OL36615850M(twisted love) , 26c15681e554b48e2a71b751c50cc7c0(... lies)
ValidationResult(match=False, confidence=15, reasons=['Author matched (100.0%)'])

"""
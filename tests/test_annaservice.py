from app.services.annaservice import AnnaService

service = AnnaService()

book = service.get_book("7aa81102d79dd065946b9778ebb8e217")

#
print (book)
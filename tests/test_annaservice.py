from app.services.annaservice import AnnaService

service = AnnaService()

book = service.get_book("669163b9d6cfc18d814cc80f1cf699e9")

#
print (book)
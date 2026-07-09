from app.services.openlibraryservice import OpenLibraryService

service = OpenLibraryService()

book = service.get_book("OL37758586M")

print (book)
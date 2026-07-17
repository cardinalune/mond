from app.services.openlibrary import OpenLibraryService

service = OpenLibraryService()

book = service.get_book("OL37758586M")

print (book)
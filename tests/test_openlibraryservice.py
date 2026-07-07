from app.services.openlibraryservice import OpenLibraryService

service = OpenLibraryService()

book = service.get_book("OL38446297M")

print (book)
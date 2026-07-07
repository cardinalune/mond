from app.services.openlibraryservice import OpenLibraryService

service = OpenLibraryService()

book = service.get_book("OL26423923M")

print (book)
from app.services.anna import AnnaService

service = AnnaService()

book = service.get_book("03f1e5747bb87f26b42ab1cbf8c610db")

#
print (book)
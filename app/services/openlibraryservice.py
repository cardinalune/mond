import requests
from app.models.book import Book
from app.models.identifiers import Identifiers


class OpenLibraryService:

    def __init__(self) -> None:
        self.headers={
            "User-Agent": "Mond/1.0 (cardinalune@gmail.com)"
        }
        

    def get_book(self, olid) -> Book | None:
        url = f"https://openlibrary.org/books/{olid}.json"


        response= requests.get(
            url,
            headers=self.headers,
            timeout=10
        )


        if (response.status_code)==200:
            
            data = response.json()
            external_ids = data.get("identifiers", {})


            #BOOKS
            title = data.get("title")
            full_title = data.get("full_title")
            authors = []

            for author in data.get("authors", []):
                authors.append(author["key"].split("/")[-1])            
            publish_date = data.get("publish_date" )
            publishers = data.get("publishers" , [])
            languages = []

            for language in data.get("languages", []):
                languages.append(language["key"].split("/")[-1])
            pages = data.get("number_of_pages")
            if pages is None:
                pages = data.get("pagination")
            series = data.get("series" , [])


            #IDENTIFIER
            oleid = data["key"].split("/")[-1]                # Edition ID
            works = data.get("works", [])               #work ID

            if works:
                olwid = works[0]["key"].split("/")[-1]
            else:
                olwid = None     # Work ID
            isbn_13 = data.get("isbn_13", [])
            isbn_10 = data.get("isbn_10", [])
            oclc = data.get("oclc_numbers", [])
            amazon = external_ids.get("amazon", [])
            goodreads = external_ids.get("goodreads", [])
            storygraph = external_ids.get("storygraph", [])
            abebooks = external_ids.get("abebooks.de", [])
            better_world_books = external_ids.get("better_world_books", [])
            alibris_id = external_ids.get("alibris_id", [])



            identifiers = Identifiers(
                olwid=olwid,
                 oleid=oleid,
                 isbn_13=isbn_13,
                 isbn_10=isbn_10,
                 oclc=oclc,
                 amazon = amazon,
                 goodreads = goodreads,
                 storygraph = storygraph,
                 abebooks=abebooks,
                 better_world_books=better_world_books,
                 alibris_id=alibris_id
            )


            book = Book(
                  title=title,
                  full_title=full_title,
                  authors=authors,
                  publish_date=publish_date,
                  publishers=publishers,
                  languages=languages,
                  pages=pages,
                  series=series,
                  identifiers=identifiers
            )

            return book
            

        return None


        
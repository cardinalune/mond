import requests
from app.models.book import Book
from app.models.identifiers import Identifiers
from app.exceptions.bookexceptions import BookNotFoundError
from app.exceptions.serviceexceptions import ExternalServiceError


class OpenLibraryService:

    def __init__(self) -> None:
        self.headers={
            "User-Agent": "Mond/1.0 (cardinalune@gmail.com)"
        }
        

    def get_book(self, olid) -> Book :
        url = f"https://openlibrary.org/books/{olid}.json"

        try:
            response= requests.get(
                url,
                headers=self.headers,
                timeout=10
            )
        except requests.Timeout:
            raise ExternalServiceError("Open Library request timed out.")
        except requests.ConnectionError:
            raise ExternalServiceError("Unable to connect to Open Library.")
        except requests.RequestException:
            raise ExternalServiceError("Unexpected error while communicating with Open Library.")
            

        if response.status_code == 404:
            raise BookNotFoundError("Book Not Found in OpenLibrary") 

        if response.status_code != 200:
            raise ExternalServiceError("Open Library returned an unexpected response")


        
            
        data = response.json()
        external_ids = data.get("identifiers", {})


        #BOOKS
        title = data.get("title")
        full_title = data.get("full_title")

        authors = []
        for author in data.get("authors", []):
            olaid = author["key"].split("/")[-1]

            author_name = self._get_author(olaid)

            if author_name:
                authors.append(author_name)    


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
            


    def _get_author(self, olaid):
        url = f"https://openlibrary.org/authors/{olaid}.json"

        try:
            response= requests.get(
                url,
                headers=self.headers,
                timeout=10
            )
        except requests.Timeout:
            raise ExternalServiceError("Open Library request timed out.")
        except requests.ConnectionError:
            raise ExternalServiceError("Unable to connect to Open Library.")
        except requests.RequestException:
            raise ExternalServiceError("Unexpected error while communicating with Open Library.")

        if response.status_code != 200:
            return None


        data = response.json()
        return data.get("name")
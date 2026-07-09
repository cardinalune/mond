import requests
from bs4 import BeautifulSoup
from pprint import pprint
from app.models.book import Book
from app.models.identifiers import Identifiers


class AnnaService:

    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mond/1.0 (cardinalune@gmail.com)"
        }

    def get_book(self, md5):
        url = f"https://annas-archive.pk/md5/{md5}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=(10,30)
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        title = self._extract_title(soup)
        authors = self._extract_authors(soup)
        codes = self._extract_codes(soup)           

        identifiers = self._extract_identifiers(codes)

        return Book(
            title=title,  # pyright: ignore[reportArgumentType]
            authors=authors,
            identifiers=identifiers
        )



    def _extract_codes(self, soup):
        soup_text = soup.find_all("a", class_="js-md5-codes-tabs-tab")

        codes = {}

        for item in soup_text:
            spans = item.find_all("span")
            
            key=spans[0].text
            value = spans[1].text

            if key not in codes:
                 codes[key] = value

            else:
                if not isinstance(codes[key] , list):
                    codes[key]= [codes[key]]

                codes[key].append(value)

        return codes



    def _extract_authors(self, soup):

        for div in soup.find_all("div"):
            classes = div.get("class", [])
            if "text-amber-900" in classes and div.has_attr("data-content"):
                return [div["data-content"]]

        return []

    def _extract_title(self, soup):

        for div in soup.find_all("div"):
            classes = div.get("class", [])
            if "text-violet-900" in classes and div.has_attr("data-content"):
                return div["data-content"]

        return None


    def _extract_identifiers(self, codes):

        identifiers = Identifiers()

#----------------------------MD5------------------------------------
        identifiers.md5 = codes.get("MD5")
        

#----------------------------ISBN-10------------------------------------
        if  isinstance(codes.get("ISBN-10") , str):
           identifiers.isbn_10.append(codes.get("ISBN-10"))
        else:    
            for isbn10s in codes.get("ISBN-10" , []):
                if isbn10s not in identifiers.isbn_10:
                    identifiers.isbn_10.append(isbn10s)


#----------------------------ISBN-13------------------------------------
        if isinstance(codes.get("ISBN-13") , str):
            identifiers.isbn_13.append(codes.get("ISBN-13"))
        else:    
            for isbn13s in codes.get("ISBN-13" , []):
                if isbn13s not in identifiers.isbn_13:
                    identifiers.isbn_13.append(isbn13s)


#----------------------------OLEID------------------------------------
        try:
            if codes.get("Open Library")[0].endswith("M"):
                identifiers.oleid = codes.get("Open Library")[0]
            else:identifiers.oleid = codes.get("Open Library")[1] 
        except Exception as e:
            identifiers.oleid="not found"  
       

#----------------------------OLWID------------------------------------
        try:
            if codes.get("Open Library")[1].endswith("W"):
                identifiers.olwid = codes.get("Open Library")[1]
            else:identifiers.olwid = codes.get("Open Library")[0]
        except Exception as e:
            identifiers.olwid="not found"

#---------------------------Source records--------------------------------
        SOURCE_MAP = {
            "amazon": "amazon",
            "goodreads": "goodreads",
            "storygraph": "storygraph",
            "abebooks": "abebooks",
            "alibris": "alibris_id",
            "bwb": "better_world_books"
    }

        if isinstance(codes.get("Open Library Source Record") , str):
            source, value = codes.get("Open Library Source Record").split(":", 1)
            field_name = SOURCE_MAP.get(source)
            if field_name:
                getattr(identifiers, field_name).append(value)

        else:        
            for record in codes.get("Open Library Source Record", []):

                source, value = record.split(":", 1)

                field_name = SOURCE_MAP.get(source)

                if field_name:
                    getattr(identifiers, field_name).append(value)

 #----------------------------OCLC------------------------------------
        if isinstance(codes.get("OCLC") , str):
            identifiers.oclc.append(codes.get("OCLC"))
        else:    
            for oclcs in codes.get("OCLC" , []):
                if oclcs not in identifiers.oclc:
                    identifiers.oclc.append(oclcs)            

        return identifiers    
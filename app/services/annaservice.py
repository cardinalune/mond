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
        url = f"https://annas-archive.gl/md5/{md5}"

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
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

        identifiers.md5 = codes.get("MD5")

        return identifiers    
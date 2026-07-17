from app.models.validationresult import ValidationResult
from app.models.identifiers import Identifiers
from app.models.book import Book
from rapidfuzz import fuzz
import re

class Validator:

    def _normalize(self, text):
        if text is None:
            return ""

        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)   # Remove punctuation
        text = " ".join(text.split())         # Remove extra spaces

        return text


    def _normalize_identifier(self, value):
        return value.replace("-", "").replace(" ", "")


    def validate(self , source , target):
        if self._compare_oleid(source , target):
           return ValidationResult(
                match=True,
                confidence=100,
                reasons=["OLEID matched"]
            )

        identifier_matches = self._compare_identifiers(source, target)

        title_score = self._compare_title(source, target)

        author_score = self._compare_authors(source, target)

        confidence, reasons = self._calculate_score(
        identifier_matches,
        title_score,
        author_score
    )

        return ValidationResult(
            match=confidence >= 70,
            confidence=confidence,
            reasons=reasons
    )    

    
    def _compare_oleid(self , source , target):
        if source.identifiers.oleid == target.identifiers.oleid:
            return True
        return False


    def _compare_identifiers(self, source, target):
        matches = []

        IDENTIFIER_FIELDS = [
            ("isbn_13", "ISBN-13"),
            ("isbn_10", "ISBN-10"),
            ("oclc", "OCLC"),
            ("goodreads", "Goodreads"),
            ("amazon", "Amazon"),
            ("storygraph", "StoryGraph"),
            ("abebooks", "AbeBooks"),
            ("alibris_id", "Alibris"),
            ("better_world_books", "Better World Books"),
        ]

        for field, label in IDENTIFIER_FIELDS:

            source_values = getattr(source.identifiers, field)
            target_values = getattr(target.identifiers, field)

        # Normalize only ISBNs
            if field in ("isbn_13", "isbn_10"):
                source_values = {self._normalize_identifier(v) for v in source_values}
                target_values = {self._normalize_identifier(v) for v in target_values}

        # If either side has no values, skip it.
            if not source_values or not target_values:
                continue

        # Check if they share at least one identifier.
            if set(source_values) & set(target_values):
                matches.append(f"{label} matched")

        return matches

    def _compare_title(self ,  source , target):
        
        source_title = self._normalize(source.title)
        target_title = self._normalize(target.title)

        ratio=fuzz.token_set_ratio(source_title , target_title)

        return ratio


    def _compare_authors(self ,  source , target):

        if not source.authors or not target.authors:
            return 0


        source_author = self._normalize(source.authors[0])
        target_author = self._normalize(target.authors[0])

        ratio=fuzz.token_set_ratio(source_author , target_author)

        return ratio


    def _calculate_score(self, identifier_matches, title_score, author_score):

        score = 0
        reasons = []

        IDENTIFIER_SCORES = {
            "ISBN-13 matched": 50,
            "ISBN-10 matched": 40,
            "OCLC matched": 30,
            "Goodreads matched": 10,
            "Amazon matched": 10,
            "StoryGraph matched": 10,
            "AbeBooks matched": 10,
            "Alibris matched": 10,
            "Better World Books matched": 10,
        }

    
        for match in identifier_matches:
            score += IDENTIFIER_SCORES.get(match, 0)
            reasons.append(match)

    
        if title_score >= 95:
            score += 20
            reasons.append(f"Title matched ({title_score:.1f}%)")
        elif title_score >= 85:
            score += 10
            reasons.append(f"Similar title ({title_score:.1f}%)")

    
        if author_score >= 95:
            score += 15
            reasons.append(f"Author matched ({author_score:.1f}%)")
        elif author_score >= 85:
            score += 8
            reasons.append(f"Similar author ({author_score:.1f}%)")

    
        confidence = min(score, 100)

        return confidence, reasons

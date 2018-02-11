from google import google
from difflib import SequenceMatcher


def limit_32_words(string: str) -> str:
    """
    Takes a string and shortens it down to 32 words for the google search

    @param string, a string to be shortened
    @return a 32 word string
    """
    return_str = ""
    space_accum = 0
    for c in string:
        if space_accum == 32:
            break

        if c == " ":
            return_str += c
            space_accum += 1

        else:
            return_str += c

    return return_str


def compare_strings(string1: str, string2: str) -> float:
    """
    Compares the similarity between two strings and returns a float representation of their similarity

    @param string1, a string to be compared
    @param string2, a string to be compared
    @return a float containing the percentage similarity between the two strings
    """
    return SequenceMatcher(None, string1, string2).ratio()


def get_google_search_feature(article_contents: str) -> float:
    """
    Takes a quote from an article, uses a Google Search API to get the first page of similar results, compares every
     result to the quote, and returns the average similarity of every result. Higher = more suspicious.

    @param article_contents, a string containing a random quote from an article.
    @return a float average of similarity between the article quote and the descriptions of the first page google search
     results.
    """
    article_contents = limit_32_words(article_contents)
    search_results = google.search(article_contents, 1)
    similarity_accum = 0

    for result in search_results:
        similarity_accum += compare_strings(article_contents.strip(), result.description.strip())

    return similarity_accum / len(search_results)

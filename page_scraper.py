import requests
from readability import Document
from bs4 import BeautifulSoup


def get_article_content(url: str) -> tuple:
    """
    Takes a link to an article, gets the reader view HTML, and then strips this HTML string of any remaining HTML tags

    @param url, a string containing a link to an article
    @return a tuple with the title and text of the article
    """
    response = requests.get(url)
    doc = Document(response.text)
    title = doc.title()
    soup = BeautifulSoup(doc.summary(), "lxml")
    text = soup.get_text()

    return title, text

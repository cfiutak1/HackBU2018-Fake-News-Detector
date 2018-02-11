import google_search
import page_scraper
import text_algorithm
import whois_algorithm


def get_results(url: str) -> dict:
    """
    Runs each algorithm on the input article, and returns all the results in a dictionary

    @param url, a string containing the URL of an article
    @return a dictionary containing each algorithm's results
    """
    article_contents = page_scraper.get_article_content(url)
    whois_dict = whois_algorithm.get_whois_features(url)
    text_dict = text_algorithm.get_text_features(article_contents)
    google_var = google_search.get_google_search_feature(article_contents)

    return {
        "location_value": whois_dict["location_value"],
        "age_value": whois_dict["age_value"],
        "flesch_reading": text_dict["flesch_reading"],
        "flesch_kincaid": text_dict["flesch_kincaid"],
        "coleman_liau": text_dict["coleman_liau"],
        "typos_to_words": text_dict["typos_to_words"],
        "percent_difficult_words": text_dict["percent_difficult_words"],
        "google_search_similarity": google_var,
    }

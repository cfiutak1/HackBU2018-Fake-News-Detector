import google_search
import page_scraper
import text_algorithm
import whois_algorithm
import json


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


def populate_json(jsonfile, jsontarget):
    
    for line in jsonfile:
        articlebody = page_scraper.get_article_content(jsontarget[line]["URL"])
        articledata = text_algorithm.get_text_features(articlebody)

        jsontarget[line]["flesch_reading"] = articledata["flesch_reading"]
        jsontarget[line]["flesch_kincaid"] = articledata["flesch_kincaid"]
        jsontarget[line]["coleman_liau"] = articledata["coleman_liau"]
        jsontarget[line]["typo_pct"] = articledata["typos_to_words"]
        jsontarget[line]["diff_word_pct"] = articledata["percent_difficult_words"]
        jsontarget[line]["google_search_hits"] = google_search.get_google_search_feature(articlebody)
        jsontarget[line]["whois_location"] = whois_algorithm.get_whois_features(jsonfile[line]["URL"])["location"]
        jsontarget[line]["whois_age"] = whois_algorithm.get_whois_features(jsonfile[line]["URL"])["age"]
        jsontarget[line]["fake"] = jsonfile[line]["fake"]


import google_search
import page_scraper
import text_algorithm
import whois_algorithm
import estimator
import json


def get_results(url: str) -> list:
    """
    Runs each algorithm on the input article, and returns all the results in a dictionary

    @param url, a string containing the URL of an article
    @return a dictionary containing each algorithm's results
    """
    article_contents = page_scraper.get_article_content(url)
    whois_dict = whois_algorithm.get_whois_features(url)
    text_dict = text_algorithm.get_text_features(article_contents)
    google_var = google_search.get_google_search_feature(article_contents)

    results_dict = {
        "location_value": [whois_dict["location_value"]],
        "age_value": [whois_dict["age_value"]],
        "flesch_reading": [text_dict["flesch_reading"]],
        "flesch_kincaid": [text_dict["flesch_kincaid"]],
        "coleman_liau": [text_dict["coleman_liau"]],
        "typos_to_words": [text_dict["typos_to_words"]],
        "percent_difficult_words": [text_dict["percent_difficult_words"]],
        "google_search_similarity": [google_var],
    }

    print(estimator.invoke(results_dict))

get_results("https://worldtruth.tv/clinton-estate-is-officially-a-crime-scene-as-11-more-steel-barrel-graves-are-uncovered/?utm_source=facebook&utm_medium=social&utm_campaign=SocialWarfare")

"""
print(get_results("https://www.infowars.com/poll-americans-overwhelmingly-believe-obama-improperly-surveilled-trump-campaign/"))
def populate_json(jsonfile, jsontarget):
    fptr1 = open(jsonfile, "r")
    existing_json = json.load(fptr1)
    fptr1.close()

    article_list = []
    # print(existing_json)
    for article in existing_json:
        try:
            new_article = {}
            article_info = get_results(article["url"])
            new_article["location_value"] = article_info["location_value"]
            new_article["age_value"] = article_info["age_value"]
            new_article["flesch_reading"] = article_info["flesch_reading"]
            new_article["flesch_kincaid"] = article_info["flesch_kincaid"]
            new_article["coleman_liau"] = article_info["coleman_liau"]
            new_article["typos_to_words"] = article_info["typos_to_words"]
            new_article["percent_difficult_words"] = article_info["percent_difficult_words"]
            new_article["google_search_similarity"] = article_info["google_search_similarity"]

            article_list.append(new_article)

        except Exception as e:
            print(article["url"])
            print(e)

    fptr2 = open(jsontarget, "w")
    json.dump(article_list, fptr2, indent=4)
    fptr2.close()

# populate_json("fakenews_testing.json", "fakenews_testing_set.json")

def add_fake_news_tags(jsonfile: str) -> None:
    fptr = open("fakenews_testing_set.json", "r")
    article_list = json.load(fptr)

    print(article_list)
    print(len(article_list))
    print("="*20)
    for i in range(25):
        # print("FAKE", article_list[i]["url"])
        print(i)
        article_list[i]["fake"] = 1

    for i in range(25,50):
        # print("REAL", article_list[i]["url"])
        print(i)
        article_list[i]["fake"] = 0

    fptr2 = open("fakenews_testing_set2.json", "w")
    json.dump(article_list, fptr2, indent=4)
    fptr.close()


"""
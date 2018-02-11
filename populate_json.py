import json

def populate_json(jsonfile, jsontarget):
    
    for line in jsonfile:
        articlebody = get_article_content(jsontarget[line]["URL"])
        articledata = get_text_features(articlebody)

        jsontarget[line]["flesch_reading"] = articledata["flesch_reading"]
        jsontarget[line]["flesch_kincaid"] = articledata["flesch_kincaid"]
        jsontarget[line]["coleman_liau"] = articledata["coleman_liau"]
        jsontarget[line]["typo_pct"] = articledata["typos_to_words"]
        jsontarget[line]["diff_word_pct"] = articledata["percent_difficult_words"]
        jsontarget[line]["google_search_hits"] = get_google_search_feature(articlebody)
        jsontarget[line]["whois_location"] = get_whois_features(jsonfile[line]["URL"])["location"]
        jsontarget[line]["whois_age"] = get_whois_features(jsonfile[line]["URL"])["age"]
        jsontarget[line]["fake"] = jsonfile[line]["fake"]


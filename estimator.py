from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import argparse
import tensorflow as tf
import news_data
import quick_scripts
import google_search
import whois_algorithm
import text_algorithm
import page_scraper
import time

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=50, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')


def get_article_dict(url: str) -> dict:
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

    return results_dict

"""
def main(argv):
    print("ARGV", argv)
    args = parser.parse_args(argv[1:])

    print("ARGS", args)
    # Fetch the data
    (train_features, train_label), (test_features, test_label) = news_data.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_features.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 7, 7 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 7 nodes each.
        hidden_units=[7, 7],
        # The model must choose between 2 classes.
        n_classes=2)

    # Train the Model.
    classifier.train(input_fn=lambda: news_data.train_input_fn(
        train_features, train_label, args.batch_size),
                     steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda: news_data.eval_input_fn(test_features, test_label,
                                                 args.batch_size))

    # print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    # expected = ['Fake', 'Real', 'Fake']
    predict_features = ARTICLE_DICT
    print(ARTICLE_DICT)

    predictions = classifier.predict(
        input_fn=lambda: news_data.eval_input_fn(predict_features,
                                                 labels=None,
                                                 batch_size=50))

    list_predictions = list(predictions)
    # print(list_predictions)
    # print(list_predictions[0])
    class_id = list_predictions[0]['class_ids'][0]
    # print(news_data.TYPES[class_id])
    # print()

    RETURN_VAL = [news_data.TYPES[class_id], list_predictions[0]['probabilities'][class_id] * 100]
    # print(args)
    # for pred_dict, expec in zip(predictions, expected):
    #     template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')
    #
    #     class_id = pred_dict['class_ids'][0]
    #     probability = pred_dict['probabilities'][class_id]
    #
    #     print(template.format(news_data.TYPES[class_id],
    #                           100 * probability, expec))

    # return (news_data.TYPES[class_id], 100* probability)
"""

def network_result(article_dict: dict):
    # Fetch the data
    (train_features, train_label), (test_features, test_label) = news_data.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_features.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 7, 7 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 7 nodes each.
        hidden_units=[7, 7],
        # The model must choose between 2 classes.
        n_classes=2)

    # Train the Model.
    classifier.train(input_fn=lambda: news_data.train_input_fn(
        train_features, train_label, 50),
                     steps=1000)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda: news_data.eval_input_fn(test_features, test_label,
                                                 50))

    # Generate predictions from the model
    predict_features = article_dict

    predictions = classifier.predict(
        input_fn=lambda: news_data.eval_input_fn(predict_features,
                                                 labels=None,
                                                 batch_size=50))

    list_predictions = list(predictions)
    class_id = list_predictions[0]['class_ids'][0]

    return [news_data.TYPES[class_id], list_predictions[0]['probabilities'][class_id] * 100]


def get_result(url: str) -> list:
    tf.logging.set_verbosity(tf.logging.INFO)
    article_dict = get_article_dict(url)

    return network_result(article_dict)

t1 = time.time()
print(get_result("https://worldtruth.tv/clinton-estate-is-officially-a-crime-scene-as-11-more-steel-barrel-graves-are-uncovered/?utm_source=facebook&utm_medium=social&utm_campaign=SocialWarfare"))
print(time.time() - t1)

print(get_result("https://www.nytimes.com/2018/02/10/us/politics/tax-cuts-election-message-trump.html"))
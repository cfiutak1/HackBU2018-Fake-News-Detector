from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf

import news_data

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=50, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int,
                    help='number of training steps')

PREDICT_FEATURES = {}
RETURN_VAR = []

def main(argv):
    args = parser.parse_args(argv[1:])

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
    classifier.train(input_fn=lambda:news_data.train_input_fn(
					train_features, train_label, args.batch_size),
					steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:news_data.eval_input_fn(test_features, test_label,
                                                args.batch_size))

    # print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

    # Generate predictions from the model
    # expected = ['Fake', 'Real', 'Fake']
    # predict_features = {
    #     'location_value': [0],
    #     'age_value': [-9.437],
    #     'flesch_reading': [53.21],
    #     'flesch_kincaid': [10.3],
    #     'coleman_liau': [14.38],
    #     'typos_to_words': [0.09748427672955975],
    #     'percent_difficult_words': [0.24633123689727462],
    #     'google_search_similarity': [0.04065033090111088]
    # }

    predict_features = PREDICT_FEATURES

    predictions = classifier.predict(
        input_fn=lambda:news_data.eval_input_fn(predict_features,
                                                labels=None,
                                                batch_size=args.batch_size))

    list_predictions = list(predictions)
    # print(list_predictions)
    # print(list_predictions[0])
    class_id = list_predictions[0]['class_ids'][0]
    # print(news_data.TYPES[class_id])
    # print()

    RETURN_VAR = [news_data.TYPES[class_id], list_predictions[0]['probabilities'][class_id] * 100]
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


def invoke(results_dict: dict) -> list:
    PREDICT_FEATURES = results_dict
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
    return RETURN_VAR

from flask import Flask, render_template, redirect, request
import estimator
app = Flask(__name__)


@app.route("/")


def hello_world():
    title = "Fake News"
    heading = "Fake News Detector"
    return render_template('index.html')


@app.route('/submit', methods=['POST'])


def submit():
    if request.method == 'POST':
        url = request.form['url']
        #new_url = url[::-1]
    # -->should be something here that takes data from the other file <--

    result = estimator.get_result(url)
    result_list = [result[0], result[1]]
    real_fake = result_list[0]
    percent = result_list[1]
    percent_str = str(percent)
    percent_str = percent_str[:4]
    return render_template('url_text.html', percent=percent, percent_str = percent_str, real_fake= real_fake)

if __name__ == "__main__":
    app.run()
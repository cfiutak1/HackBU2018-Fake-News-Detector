from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/")


def hello_world():
    title = "Fake News"
    heading = "Fake News Detector"
    return render_template('index.html')


@app.route('/submit', methods=['POST'])


def submit():
    if request.method == 'POST':
        url = str(request.form['url'])
        #new_url = url[::-1]
    # --> should be something here that takes data from the other file <--
    percent = 0.9
    return render_template('url_text.html', percent= percent)

if __name__ == "__main__":
    app.run()
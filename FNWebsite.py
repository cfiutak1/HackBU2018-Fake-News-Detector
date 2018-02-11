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
        new_url = url[::-1]
        print(new_url)
    return render_template('url_text.html', new_url= new_url)

if __name__ == "__main__":
    app.run()
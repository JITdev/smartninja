import datetime

from flask import Flask, render_template

app = Flask(__name__, static_folder='./static', template_folder='./templates')


@app.route("/")
def index():
    text = "Message from the handler."
    year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    return render_template("index.html", some_text=text, current_year=year, cities=cities)


@app.route("/about-me")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()
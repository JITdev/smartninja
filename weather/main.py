import requests
import json

from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_folder='./static', template_folder='./templates')


@app.route("/")
def index():
    query = request.args.get('city', 'London,UK')

    unit = "metric"  # use "imperial" for Fahrenheit
    api_key = "7c5fe4b501cba91a84cca4170f89ec0f"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&units={unit}&appid={api_key}"

    data = requests.get(url=url)  # GET request to the OpenWeatherMap API

    return render_template("index.html", data=data.json())


if __name__ == '__main__':
    d = {'a': 'b'}
    json.dumps(d)
    json.loads('{"a": "b"}')
    app.run(port=5001)
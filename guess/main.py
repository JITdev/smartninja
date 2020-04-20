
import random

from flask import Flask, render_template, request, make_response

app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = 'any_random_string'


@app.route("/", methods=['GET', 'POST'])
def index():
    response = None

    # check if there is already a cookie named secret_number
    if request.method == "GET":
        secret_number = request.cookies.get("secret_number")

        response = make_response(render_template("index.html"))
        if not secret_number:  # if not, create a new cookie
            new_secret = random.randint(1, 30)
            response.set_cookie("secret_number", str(new_secret))

    elif request.method == "POST":
        guess = int(request.form.get("guess"))
        secret_number = int(request.cookies.get("secret_number"))

        if guess == secret_number:
            message = f"Correct! The secret number is {secret_number}"
            response = make_response(render_template("result.html", message=message))
            # set the new secret number
            response.set_cookie("secret_number", str(random.randint(1, 30)))

        elif guess > secret_number:
            message = "Your guess is not correct... try something smaller."
            response = render_template("result.html", message=message)
        elif guess < secret_number:
            message = "Your guess is not correct... try something bigger."
            response = render_template("result.html", message=message)

    return response


if __name__ == '__main__':
    app.run()

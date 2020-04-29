import datetime
import uuid

from flask import Flask, render_template, request, redirect, url_for, make_response
from .models import Session, User, db
from .password import is_correct_password, hash_new_password

app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.secret_key = 'random string'
db.create_all()  # create (new) tables in the database


@app.route("/")
def index():
    # email_address = request.cookies.get("email")
    session_cookie = request.cookies.get("session")

    if session_cookie:
        session = db.query(Session).filter_by(session=session_cookie).first()
        if session:
            user = db.query(User).filter_by(id=session.user_id).first()

    else:
        user = None

    return render_template("index.html", user=user)


@app.route("/register", methods=['GET'])
def register_get():
    return render_template('register.html')

@app.route("/register", methods=['POST'])
def register():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    password = request.form.get("user-password")

    # hash the password
    salt, hashed_password = hash_new_password(password)

    # create a User object
    user = User(name=name, email=email, password=hashed_password, salt=salt)

    # save the user object into a database
    db.add(user)
    db.commit()

    # save user's email into a cookie
    response = make_response(redirect(url_for('index')))

    session_token = str(uuid.uuid4().hex)

    session = Session(user_id=user.id, session=session_token)
    db.add(session)
    db.commit()

    response.set_cookie("session", session_token)

    return response


@app.route("/about-me", methods=['GET', 'POST'])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response


@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")


if __name__ == '__main__':
    app.run()
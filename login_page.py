import os
import pathlib

import requests
from flask import Flask, session, abort, redirect, request, render_template
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from track_info import user_request_list
from storage_try_1 import register_info

app = Flask("Google Login App")
app.secret_key = "CodeSpecialist.com"

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "342165659797-vph8as7kcplqps7hbgf4imo29qvb0vdt.apps.googleusercontent.com"
client_secrets_file = os.path.join(
    pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper


@app.route("/login")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    return redirect("/protected_area")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/")
def index():
    return render_template("groba.html")
#"Hello from Grobage <a href='/login'><button>Login</button></a>"


@app.route("/protected_area")
@login_is_required
def protected_area():
    data = user_request_list()
    # return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
    # return render_template('home.html', data=data)
    return render_template('home.html')


@app.route("/get_img/<imgId>")
def get_image(imgId):
    info = user_request_list()
    print("----------------------")
    print(info)
    return imgId


@app.route("/spacer", methods=["GET", "POST"])
def spacer_login():
    if request.method == "POST":

        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        service_name = request.form.get("company")
        Area_info = request.form.get("area_code")
        contact_in = request.form.get("phone")
        plant_c = request.form.get("subject")

        image_get = request.form.get("exampleFormControlFile1")

        name_info = first_name + last_name
        register_info(name_info, service_name, Area_info,
                      contact_in, plant_c, image_get)

    return render_template("form.html")


@app.route("/track")
def tracker():
    data = user_request_list()
    return render_template("page.html", data=data)


@app.route("/forum")
def forum_page():
    return render_template("forum.html")


if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_user, logout_user
from requests_oauthlib import OAuth2Session

from app import app
from app.config import settings
from app.models import User

from .forms import RegistrationForm

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)


@auth_bp.route("/login")
def login():
    google = OAuth2Session(
        client_id=settings.GOOGLE_CLIENT_ID,
        scope=settings.GOOGLE_SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT,
    )
    authorization_url, state = google.authorization_url(
        settings.GOOGLE_AUTHORIZATION_BASE_URL,
        access_type="offline",
        prompt="select_account",
    )

    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/authorize")
def authorize():
    google = OAuth2Session(
        settings.GOOGLE_CLIENT_ID,
        redirect_uri=settings.GOOGLE_REDIRECT,
        state=session["oauth_state"],
    )
    token = google.fetch_token(
        token_url=settings.GOOGLE_TOKEN_URL,
        client_secret=settings.GOOGLE_CLIENT_SECRET,
        authorization_response=request.url,
    )

    google = OAuth2Session(settings.GOOGLE_CLIENT_ID, token=token)
    userinfo = google.get("https://www.googleapis.com/oauth2/v1/userinfo").json()
    user = User.query.filter_by(email=userinfo["email"]).first()
    if user:
        login_user(user)
        next = request.args.get("next")
        if next is None or not next.startswith("/"):
            next = url_for("homepage")
        return redirect(next)
    else:
        return redirect(
            url_for(
                "auth.register",
                access_token=token["access_token"],
                token_type=token["token_type"],
            )
        )


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@auth_bp.route("/register/<access_token>", methods=["GET", "POST"])
def register(access_token: str):
    token = {"access_token": access_token, "token_type": request.args["token_type"]}
    google = OAuth2Session(client_id=settings.GOOGLE_CLIENT_ID, token=token)
    userinfo = google.get("https://www.googleapis.com/oauth2/v1/userinfo").json()
    form = RegistrationForm()
    form.email.data = userinfo.get("email")
    if form.validate_on_submit():
        username_valid = User.query.filter_by(username=form.username.data).first()
        if username_valid:
            flash("A user with this username already exists", category="danger")
            return render_template("register.html", form=form)
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.save()
            flash("Your account has been created successfully", category="success")
            login_user(user)
            return redirect(url_for("homepage"))
    return render_template("register.html", form=form)

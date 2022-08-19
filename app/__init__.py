from authlib.integrations.flask_client import OAuth
from flask import Flask, redirect, render_template, session, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    fresh_login_required,
    login_required,
)
from flask_sqlalchemy import SQLAlchemy

from app.config import settings

app = Flask(__name__)
app.config.from_object(settings)

CONF_URL = "https://accounts.google.com/.well-known/openid-configuration"
oauth = OAuth(app)
oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url=CONF_URL,
    access_type="offline",
    prompt="consent",
    client_kwargs={"scope": "openid email profile"},
)

# Database
db = SQLAlchemy(app)

# Login Manager
login_manager = LoginManager(app)
# login_manager.refresh_view = "auth.login"
# login_manager.needs_refresh_message = "Please log in to access this page!"
# login_manager.needs_refresh_message_category = "info"


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/protected")
@fresh_login_required
def protected():
    return render_template("protected.html")


## Blueprints
from app.views.auth import auth

app.register_blueprint(auth.auth_bp)

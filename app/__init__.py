from flask import Flask, render_template
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy

from app.config import settings

app = Flask(__name__)
app.config.from_object(settings)

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
@login_required
def protected():
    return render_template("protected.html")


# Blueprints
from app.views.auth import auth

app.register_blueprint(auth.auth_bp)  # type: ignore  # noqa

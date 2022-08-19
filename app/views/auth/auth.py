from flask import Blueprint, url_for, session, redirect, flash, request
from flask_login import logout_user, login_user

from app import app, oauth
from app.models import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)

@auth_bp.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    token = oauth.google.authorize_access_token()
    print(token)
    userinfo = token.get('userinfo')
    
    user = User.query.filter_by(email=userinfo["email"]).first()
    if user:
        login_user(user)
        next = request.args.get("next")
        if next is None or not next.startswith("/"):
            next = url_for("homepage")
        return redirect(next)
    flash(f"Error al loguearse", category="danger")
    return redirect('/')


@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect('/')
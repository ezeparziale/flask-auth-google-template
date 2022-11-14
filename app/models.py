from flask import redirect, url_for
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth.login"))


class User(db.Model, UserMixin):  # type: ignore  # noqa
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"{self.username} : {self.email} : {self.created_at}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

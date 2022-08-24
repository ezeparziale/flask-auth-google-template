from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        label="Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()],
        render_kw={"readonly": True},
    )
    submit = SubmitField(label="Create Account")

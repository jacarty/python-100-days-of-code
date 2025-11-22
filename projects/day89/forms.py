from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, URL, Email, NumberRange
from flask_ckeditor import CKEditorField


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

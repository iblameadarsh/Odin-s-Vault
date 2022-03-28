from flask_wtf import FlaskForm,
from wtforms import StringField, SubmitField,PasswordField, BooleanField
from wtforms.validators import DataRequired, length, Email, EqualTo

class Signupform(FlaskForm):
	username = StringField("Username",validaors = [DataRequired(),Length(min=2,max=20))]
	email = StringField("Email",validaors = [DataRequired(),Email()])
	password = PasswordField("Password",validaors=[DataRequired ()])
	confirm_password = PasswordField("Confirm Password",validaors=[DataRequired(),EqualTo('password')])
	submit = SubmitField("Sign Up")

class Loginform(FlaskForm):
	email = StringField("Email",validaors = [DataRequired(),Email()])
	password = PasswordField("Password",validaors=[DataRequired()])
	remember = BooleanField('Remember Me!')
	submit = SubmitField("Log In")
	

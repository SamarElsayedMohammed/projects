from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegitrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max= 25)])
    username = StringField('Username', [validators.Length(min=4, max= 25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('New Password',[validators.DataRequired(),validators.EqualTo('confirm',message='passwords must match')])
    confirm = PasswordField('repeate Password')

class LoginForm(Form):
   
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])
    password = PasswordField('Password',[validators.DataRequired()])
    
from wtforms import Form, StringField, TextAreaField, PasswordField,SubmitField,validators, ValidationError
from flask_wtf.file import FileRequired,FileAllowed, FileField,FileAllowed
from flask_wtf import FlaskForm
from .model import Register




class CustomerRegisterForm(FlaskForm):
    name = StringField('Name: ')
    username = StringField('Username: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(), validators.EqualTo('confirm', message=' Both password must match! ')])
    confirm = PasswordField('Repeat Password: ', [validators.DataRequired()])
    country = StringField('Country: ', [validators.DataRequired()])
    city = StringField('City: ', [validators.DataRequired()])
    contact = StringField('Contact: ', [validators.DataRequired()])
    address = StringField('Address: ', [validators.DataRequired()])
    zipcode = StringField('Zip code: ', [validators.DataRequired()])

    profile = FileField('Profile', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Image only please')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")

    


class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        [validators.Email(), validators.DataRequired()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = Register.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password: ', [validators.DataRequired(), validators.EqualTo('confirm_password', message=' Both password must match! ')])
    confirm_password = PasswordField('Repeat Password: ', [validators.DataRequired()])
    submit = SubmitField('Reset Password')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username: ', [validators.DataRequired(),validators.Length(min=2, max=20)])

    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    profile = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg','gif'], 'Image only please')])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This username is already in use!")
        
    def validate_email(self, email):
        if Register.query.filter_by(email=email.data).first():
            raise ValidationError("This email address is already in use!")



   




   

 

    

     

   


    


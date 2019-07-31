from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, BooleanField ,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(), Email()])
    username = StringField('Enter username',validators= [ Required()])
    password = PasswordField('password',validators=[Required(), EqualTo('password_confirm',message='password must match')])

    password_confirm = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('Tehere is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('This username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remeber me")
    submit = SubmitField('Sign in')
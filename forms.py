from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, 
from wtforms.validators import DataRequired,Length,Email,EqualTo



class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(message="This is a required field"),
                        Length(min=2,max=20) ])
    email=StringField('Email',validators=[DataRequired(message="This is a required field"),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=15)])
    confirm_password = PasswordField('COnfirm Password', validators=[DataRequired(), EqualTo(password)])
    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(message="This is a required field"),Email()])

    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=15)])
    remember=

    submit=SubmitField('Sign Up')
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired 

class AddressForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()]) 
    last_name = StringField('Last Name:', validators=[DataRequired()]) 
    address = StringField('Address:', validators=[DataRequired()]) 
    city = StringField('City:', validators=[DataRequired()]) 
    state = StringField('State:', validators=[DataRequired()]) 
    zip_code = StringField('Zip Code:', validators=[DataRequired()]) 
    submit = SubmitField('Save')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

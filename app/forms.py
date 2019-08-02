from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class NewAddressForm(FlaskForm):
   first_name = StringField('First Name', validators=[DataRequired()]) 
   last_name = StringField('Last Name', validators=[DataRequired()]) 
   addresss = StringField('Address', validators=[DataRequired()]) 
   city = StringField('City', validators=[DataRequired()]) 
   state = StringField('State', validators=[DataRequired()]) 
   zip_code = StringField('Zip_code', validators=[DataRequired()]) 
   submit = SubmitField('Add Address')

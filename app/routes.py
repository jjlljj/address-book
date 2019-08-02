from flask import render_template
from app import app
from app.models import Address
from app.forms import NewAddressForm

@app.route('/')
@app.route('/index')

def index():
    return "Hello Flask App"

@app.route('/address_book', methods=['GET'])

def address_book():
    addresses = Address.query.all()
    return render_template('address_book.html', addresses=addresses)


@app.route('/address_book/new', methods=['GET', 'POST'])
def add_address():
    form=NewAddressForm()
    return render_template('new_address.html', form=form)

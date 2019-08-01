from flask import render_template
from app import app
from app.models import Address

@app.route('/')
@app.route('/index')

def index():
    return "Hello Flask App"

@app.route('/address_book', methods=['GET'])

def address_book():
    addresses = Address.query.all()
    return render_template('address_book.html', addresses=addresses)

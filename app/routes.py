from flask import render_template, flash, redirect, url_for
from app import app, db
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
    if form.validate_on_submit():


        address = Address(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            zip_code = form.zip_code.data,
        )
        db.session.add(address)
        db.session.commit()
        flash('New Address Added')
            # form.first_name.data, 
            # form.last_name.data
        return redirect(url_for('address_book'))

    return render_template('new_address.html', form=form)


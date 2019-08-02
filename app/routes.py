from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db
from app.models import Address
from app.forms import AddressForm

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
    form=AddressForm()
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

        return redirect(url_for('address_book'))

    return render_template('address_form.html', form=form, form_title='Add A New Address')

@app.route('/address_book/edit/<address_id>', methods=['GET', 'POST'])
def edit_address(address_id):
    address = Address.query.get(address_id)
    form=AddressForm()

    if form.validate_on_submit():
        address.first_name = form.first_name.data 
        address.last_name = form.last_name.data 
        address.address = form.address.data 
        address.city = form.city.data 
        address.state = form.state.data 
        address.zip_code = form.zip_code.data 

        db.session.commit()

        flash('Saved')

        return redirect(url_for('address_book'))

    form.first_name.data = address.first_name
    form.last_name.data = address.last_name
    form.address.data = address.address
    form.city.data = address.city
    form.state.data = address.state
    form.zip_code.data = address.zip_code

    return render_template('address_form.html', form=form, form_title="Edit Address")


@app.route('/api/address_book/edit/<address_id>', methods=['DELETE'])
def delete_address(address_id):
    address = Address.query.get(address_id)

    if request.method == 'DELETE':
        db.session.delete(address)
        db.session.commit()

        return jsonify(
            deleted=True,
            success=True
        )







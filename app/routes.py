from flask import render_template, flash, redirect, url_for, jsonify, request
from app import app, db
from app.models import Address, User
from app.forms import AddressForm, LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('address_book'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            login_error = 'User Not Found' if user is None else 'Incorrect Password'
            return render_template('login_form.html', title='Sign In', form=form, login_error=login_error)
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('address_book')
        return redirect(next_page)
    return render_template('login_form.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('address_book'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=False)
        return redirect(url_for('address_book'))
    return render_template('registration_form.html', title='Register', form=form)

@app.route('/address_book', methods=['GET'])
@login_required
def address_book():
    addresses = Address.query.filter_by(user_id=current_user.id)
    return render_template('address_book.html', addresses=addresses, page_title=current_user.username+"'s Address Book")


@app.route('/address_book/new', methods=['GET', 'POST'])
@login_required
def add_address():
    form=AddressForm()
    if form.validate_on_submit():
        address = Address(
            first_name = form.first_name.data.title(),
            last_name = form.last_name.data.title(),
            address = form.address.data.title(),
            city = form.city.data.title(),
            state = form.state.data,
            zip_code = form.zip_code.data,
            user_id = current_user.id
        )
        db.session.add(address)
        db.session.commit()

        return redirect(url_for('address_book'))

    return render_template('address_form.html', form=form, form_title='Add A New Address')

@app.route('/address_book/edit/<address_id>', methods=['GET', 'POST'])
@login_required
def edit_address(address_id):
    address = Address.query.get(address_id)
    if not address or address.user_id != current_user.id:
        return redirect(url_for('address_book'))

    form=AddressForm()
    if form.validate_on_submit():
        address.first_name = form.first_name.data.title()
        address.last_name = form.last_name.data.title()
        address.address = form.address.data.title()
        address.city = form.city.data.title() 
        address.state = form.state.data
        address.zip_code = form.zip_code.data 

        db.session.commit()
        return redirect(url_for('address_book'))

    form.first_name.data = address.first_name
    form.last_name.data = address.last_name
    form.address.data = address.address
    form.city.data = address.city
    form.state.data = address.state
    form.zip_code.data = address.zip_code

    return render_template(
        'address_form.html', 
        form=form, 
        form_title="Edit Address", 
    )


@app.route('/api/address_book/edit/<address_id>', methods=['DELETE'])
@login_required
def delete_address(address_id):
    address = Address.query.get(address_id)
    if not address or address.user_id != current_user.id:
        return jsonify(
            deleted=False,
            success=False
        )

    if request.method == 'DELETE':
        db.session.delete(address)
        db.session.commit()

        return jsonify(
            deleted=True,
            success=True
        )







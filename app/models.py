from app import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    zip_code = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Address {}>'.format(self.first_name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    addresses = db.relationship('Address', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)   

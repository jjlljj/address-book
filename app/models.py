from app import db

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    address = db.Column(db.String(128))
    zip_code = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))

    def __repr__(self):
        return '<Address {}>'.format(self.first_name)


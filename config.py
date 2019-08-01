import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fa8a94ca-b7cd-45e6-95da-6a85475f2945'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

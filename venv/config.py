import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:123456@127.0.0.1/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
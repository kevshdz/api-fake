import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://user:password@localhost/name_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

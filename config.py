import os

basedir = os.path.abspath((os.path.dirname(__file__)))
MIGRATION_DIR = os.path.join(basedir, 'library_app/migrations')


class Config:
    DEBUG = True
    SECRET_KEY = 'secret key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATION = False

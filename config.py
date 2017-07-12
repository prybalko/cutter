from os.path import abspath, dirname, join


PROJECT_DIR = abspath(dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(PROJECT_DIR, 'cutter.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = '6,DF"kjrQ!7S&_Gz`C>7vh>}5V9Qr;'

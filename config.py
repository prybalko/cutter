from os.path import abspath, dirname, join


DEBUG = True

PROJECT_DIR = abspath(dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(PROJECT_DIR, 'cutter.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False

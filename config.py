from os.path import abspath, dirname, join


DEBUG = True

PROJECT_DIR = abspath(dirname(__file__))
REPO_DIR = dirname(PROJECT_DIR)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(REPO_DIR, 'cutter.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# what_to_watch/settings.py

import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    JSON_AS_ASCII = False


BASE_URL = 'http://localhost/'
CUSTOM_ID_RE = '^[a-zA-Z0-9]+$'
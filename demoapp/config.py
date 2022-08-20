import os

DEBUG = False
SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/huyen_test'

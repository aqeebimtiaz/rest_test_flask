import os
basedir = os.path.abspath(os.path.dirname(__file__))

# DATABASE SETTINGS
pg_db_username = 'postgres'
pg_db_password = 'postgres'
pg_db_name = 'rest_test_db'
pg_db_hostname = 'localhost'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    # SQLALCHEMY_DATABASE_URI = os.environ["postgresql://localhost/rest_test_db"]

    SQLALCHEMY_DATABASE_URI = os.environ["postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=pg_db_username, DB_PASS=pg_db_password, DB_ADDR=pg_db_hostname, DB_NAME=pg_db_name)]
    # SQLALCHEMY_DATABASE_URI = os.environ['postgres://xzmwzpgo:qzwsnKvukTb8GTuBYL-SH3RTgEVhIAtN@john.db.elephantsql.com:5432/xzmwzpgo']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

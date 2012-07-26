# TODO: split these out into separate files

class BaseConfig():
    SECRET_KEY = 'asdf'

    INSTALLED_APPS = (
        'default',
    )

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False

class TestConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class DevelopConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    WERKZEUG_OPTS = {
        'debug': True,
        # 'ssl_context': 'adhoc',
    }

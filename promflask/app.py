from flask import Flask

__all__ = [
    'create_app'
]

def create_app(name=__name__):
    app = Flask(name)
    load_config(app)

    if app.config['DEBUG']:
        app.debug = True

    return app

def load_config(app):
    app.config.from_object(__name__)

import logging
import os
import sys

from flask import Flask

__all__ = [
    'create_app'
]

def create_app(name=__name__):
    app = Flask(name)

    load_config(app)
    setup_logging(app)
    load_apps(app)

    if app.config.get('DEBUG', False):
        app.debug = True

    return app

def load_config(app):
    app.config.from_object(__name__)

    # app.config.from_envvar('PROMFLASK_CONFIG', silent=True)

    config = os.getenv('PROMFLASK_CONFIG')
    if config:
        app.config.from_object(config)

def load_apps(app):
    try:
        installed_apps = app.config['INSTALLED_APPS']
    except KeyError:
        return

    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + 'apps')

    for a in installed_apps:
        try:
            views = __import__('%s.views' % a, globals(), locals(), ['bp'], -1)
        except ImportError as e:
            print e
        else:
            app.register_blueprint(views.bp)

def setup_logging(app):
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    # log = logging.getLogger(__name__)
    # log.setLevel(logging.DEBUG)
    # handler = logging.StreamHandler(sys.stdout)
    # log.addHandler(handler)

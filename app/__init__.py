import flask

from .api import api
from .config import BaseConfig
from .database import db
from .routes import default

app = flask.Flask(__name__, template_folder='views')


def create_app(config_class=BaseConfig):
    """
    Create an app from config

    Args:
        config_class: Config class, defaults to base config

    Returns:
        Flask App
    """

    app.config.from_object(config_class)
    db.init_app(app)

    api.init_app(app)
    api.add_namespace(default.default_ns)

    return app

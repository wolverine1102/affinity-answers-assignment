from flask import Flask
from .extensions import ma
from .api.address import address_bp

def create_app(config_class=None):
    app = Flask(__name__)
    ma.init_app(app)

    app.register_blueprint(address_bp, url_prefix="/validate")

    return app
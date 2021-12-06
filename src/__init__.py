from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from .routes import blueprint as routes
    app.register_blueprint(routes)

    return app
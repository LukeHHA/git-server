import os
from typing import Any, Dict, Text
from flask import Flask

# internal modules
from src.actions import Actions
from src.helper import Serve_Helper


def create_app(test_config: None = None) -> Flask:
    # create and configure the app
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    act: Actions = Actions()

    # a simple page that says hello
    @app.route("/")
    def index() -> Dict:
        result: Text | None = Serve_Helper.get_binary_version("git", "-v")

        if result is None:
            git_status: str = "git was not found on this system"
        else:
            git_status: str = result

        return {"status": "running", "git": git_status}

    from . import serve

    app.register_blueprint(serve.bp)

    return app

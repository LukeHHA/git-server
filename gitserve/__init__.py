import os
from typing import Any

from flask import Flask
from src import actions


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

    act: actions.Actions = actions.Actions()

    # a simple page that says hello
    @app.route("/hello")
    def hello() -> Any:
        act.create_repo("helloworld")
        return "it may have worked"

    from . import serve

    app.register_blueprint(serve.bp)

    return app

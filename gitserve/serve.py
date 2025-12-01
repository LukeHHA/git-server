from flask import Blueprint
from src import actions

# from werkzeug.security import check_password_hash, generate_password_hash

bp: Blueprint = Blueprint("serve", __name__, url_prefix="/serve")

bp.route("/init_repo", methods=("GET", "POST"))

act: actions.Actions = actions.Actions()


def init_repo() -> None:
    act.create_repo("helloWorld")

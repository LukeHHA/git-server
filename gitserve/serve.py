from typing import Any
from flask import Blueprint
from src import actions

# from werkzeug.security import check_password_hash, generate_password_hash

bp: Blueprint = Blueprint("serve", __name__, url_prefix="/serve")

act: actions.Actions = actions.Actions()


@bp.route("/init_repo", methods=("GET", "POST"))
def init_repo() -> Any:
    act.create_repo("helloWorld")
    return "maybe it worked?"

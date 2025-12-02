from asyncio import Server
from typing import Any
from flask import Blueprint

# internal modules
from src.actions import Actions
from src.helper import Serve_Helper

# from werkzeug.security import check_password_hash, generate_password_hash

# instantiate blueprint
bp: Blueprint = Blueprint("serve", __name__, url_prefix="/serve")

act: Actions = Actions()


@bp.route("/init_repo", methods=("GET", "POST"))
def init_repo() -> Any:
    Serve_Helper.pre_check()
    return act.create_repo("helloWorld")

from flask import Blueprint

# from werkzeug.security import check_password_hash, generate_password_hash

bp: Blueprint = Blueprint("serve", __name__, url_prefix="/serve")

bp.route("/init", methods=("GET", "POST"))


def init() -> None:
    return

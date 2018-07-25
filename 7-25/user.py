from flask import Blueprint

bp =Blueprint('user',__name__,url_prefix='user')

@bp.route('/')
def index():
    return "User's Index page"
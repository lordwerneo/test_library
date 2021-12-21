from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
def index():
    return '<h1>This is main page</h1>'

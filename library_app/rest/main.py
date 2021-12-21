from flask import Blueprint

api_main = Blueprint('api', __name__)


@api_main.route('/')
@api_main.route('/index')
def index():
    return {'message': 'This is a main page for api.'}

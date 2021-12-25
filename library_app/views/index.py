from flask import Blueprint, render_template

index = Blueprint('index', __name__)


@index.route('/')
@index.route('/index')
def index_page():
    title = 'Home Page'
    return render_template('index.html', title=title)

from flask import Blueprint, request, render_template, url_for, flash, redirect
from library_app.forms import AddGenreForm, AddBookForm, UpdateGenreForm, \
    UpdateBookForm

index = Blueprint('index', __name__)


@index.route('/')
@index.route('/index')
def index_page():
    return render_template('index.html')

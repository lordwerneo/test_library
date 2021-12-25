from flask import Blueprint, request, render_template, url_for, flash, redirect
from library_app.forms import AddGenreForm, AddBookForm, UpdateGenreForm, \
    UpdateBookForm
from library_app.service import genre_service
from library_app.models import Genre

genres = Blueprint('genres', __name__)


@genres.route('/')
def genres_page():
    title = 'Genres'
    genres_list = genre_service.get_all_genres()
    if genres_list == 'Error':
        genres_list = None
    return render_template('genres.html', genres_list=genres_list, title=title)


@genres.route('/add_genre', methods=['POST', 'GET'])
def add_genre():
    form = AddGenreForm()
    if form.validate_on_submit():
        genre = genre_service.post_genre(
            name=form.name.data.lower(),
            description=form.description.data)
        if genre == 'Error':
            flash(f'Genre "{form.name.data}" already exists.', 'fail')
            return redirect(url_for('genres.genres_page'))
        flash(f'Genre "{form.name.data}" successfully added.', 'success')
        return redirect(url_for('genres.genres_page'))
    title = 'Add Genre'
    return render_template('add_genre.html', title=title, form=form)


@genres.route('/update_genre/<string:genre_name>', methods=['POST', 'GET'])
def update_genre(genre_name):
    genre_to_update = Genre.query.filter_by(name=genre_name).first()
    if not genre_to_update:
        flash(f'Genre "{genre_name}" doesn\'t exist.', 'fail')
        return redirect(url_for('genres.genres_page'))
    form = UpdateGenreForm(original_name=genre_name, name=genre_to_update.name,
                           description=genre_to_update.description)
    if form.validate_on_submit():
        genre = genre_service.put_genre(current_name=genre_name,
                                        name=form.name.data,
                                        description=form.description.data)
        if genre == 'Updated':
            flash(f'Genre "{form.name.data}" successfully updated.', 'success')
            return redirect(url_for('genres.genres_page'))
        elif genre == 'Busy':
            flash(f'GEnre "{form.name.data}" in use.', 'fail')
    title = 'Update Genre'
    return render_template('update_genre.html', title=title, form=form)


@genres.route('/delete_genre/<string:genre_name>')
def delete_genre(genre_name):
    genre_to_delete = genre_service.delete_genre(genre_name)
    if genre_to_delete == 'Error':
        flash(f'Genre "{genre_name}" does not exist.', 'fail')
        return redirect(url_for('genres.genres_page'))
    flash(f'Genre "{genre_name}" deleted.', 'warning')
    return redirect(url_for('genres.genres_page'))

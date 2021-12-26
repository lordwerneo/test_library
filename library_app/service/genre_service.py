from library_app import db

from ..models import Genre


def get_all_genres():
    genres = Genre.query.all()
    if genres:
        return [genre.to_dict() for genre in genres]
    return 'Error'


def post_genre(name, description):
    genre = Genre.query.filter_by(name=name).first()
    if not genre:
        genre = Genre(name=name, description=description)
        db.session.add(genre)
        db.session.commit()
        return
    return 'Error'


def put_genre(current_name, name, description):
    if current_name == name:
        if not Genre.query.filter_by(name=current_name).first():
            genre = Genre(name=name, description=description)
            db.session.add(genre)
            db.session.commit()
            return 'Created'
        else:
            genre = Genre.query.filter_by(name=current_name).first()
            genre.description = description
            db.session.commit()
            return 'Updated'
    else:
        if not Genre.query.filter_by(name=current_name).first():
            return 'Unknown'
        elif not Genre.query.filter_by(name=name).first():
            genre = Genre.query.filter_by(name=current_name).first()
            genre.name = name
            genre.description = description
            db.session.commit()
            return 'Updated'
        return 'Busy'

def delete_genre(name):
    genre = Genre.query.filter_by(name=name).first()
    if not genre:
        return 'Error'
    db.session.delete(genre)
    db.session.commit()


def get_genre_by_name(name):
    genre = Genre.query.filter_by(name=name).first()
    if genre:
        return genre.to_dict()
    return 'Error'


def get_genre_total_copies(name):
    genre = Genre.query.filter_by(name=name)
    if genre:
        return sum([book.copies for book in genre.books])
    return 'Error'


def get_genre_unique_books(name):
    genre = Genre.query.filter_by(name=name)
    if genre:
        return len(genre.books)
    return 'Error'

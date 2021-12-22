from flask_restful import Resource
from library_app.models import Book, Genre


class Genres(Resource):
    def get(self):
        genres = Genre.query.all()
        return {'genres': [genre.to_dict() for genre in genres]}

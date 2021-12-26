from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {'links': {
            'main': {'main': 'http://localhost:5000/api'},
            'genres': {'get': 'http://localhost:5000/api/genres',
                       'post': 'http://localhost:5000/api/genres'},
            'genre': {'get': 'http://localhost:5000/api/genre/<string:genre_'
                             'name>',
                      'put': 'http://localhost:5000/api/genre/<string:genre_'
                             'name>',
                      'delete': 'http://localhost:5000/api/genre/<string:genre'
                                '_name>'},
            'books': {'get': 'http://localhost:5000/api/books',
                      'post': 'http://localhost:5000/api/books'},
            'books_genre': {'get': 'http://localhost:5000/api/books/<string'
                                   ':genre_ name>'},
            'book': {'get': 'http://localhost:5000/api/book/<string:'
                            'book_isbn',
                     'put': 'http://localhost:5000/api/book/<string:'
                            'book_isbn',
                     'delete': 'http://localhost:5000/api/book/<string:'
                            'book_isbn'}
        }}

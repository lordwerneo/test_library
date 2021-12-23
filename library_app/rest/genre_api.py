from flask_restful import Resource, reqparse
from library_app.service import genre_service

genre_args = reqparse.RequestParser()
genre_args.add_argument("name", type=str, help="Name required", required=True)
genre_args.add_argument("description", type=str, help="Description required",
                        required=True)


class GenresList(Resource):
    def get(self):
        genres = genre_service.get_all_genres()
        if genres == 'Error':
            return {'Message': 'No genres in DB'}, 200
        return {'genres': genres}

    def post(self):
        args = genre_args.parse_args()
        if args['name'] == '' or args['description'] == '':
            return{'Message': 'Wrong data input'}, 400
        genres = genre_service.post_genre(name=args['name'],
                                          description=args['description'])
        if genres == 'Error':
            return {'Message': 'Genre already exists',
                    'link': f'/api/genre/{args["name"]}'}, 405
        return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 201


class GenresSolo(Resource):
    def get(self, name):
        genre = genre_service.get_genre_by_name(name)
        if genre == 'Error':
            return {'Message': 'No such genre'}, 404
        return {'genre': genre}, 200

    def put(self, name):
        args = genre_args.parse_args()
        if args['name'] == '' or args['description'] == '':
            return{'Message': 'Wrong data input'}, 400
        genre = genre_service.put_genre(current_name=name,
                                        name=args['name'],
                                        description=args['description'])
        if genre == 'Created':
            return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 201
        elif genre == 'Updated':
            return {'genre': args, 'link': f'/api/genre/{args["name"]}'}, 200
        elif genre == 'Unknown':
            return {'Message': f'No such genre {name} to update, or '
                               f'{args["name"]} is busy'}
        elif genre == 'Busy':
            return {'Message': f'Can\'t update genre {name},'
                               f'genre {args["name"]} already exist'}

    def delete(self, name):
        genre = genre_service.delete_genre(name)
        if genre == 'Error':
            return {'Message': 'No such genre'}, 404
        return {'Message': f'Genre {name} deleted.'}, 200

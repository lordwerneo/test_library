from flask_restful import Resource


class Index(Resource):
    def get(self):
        return {'message': 'Main API page'}

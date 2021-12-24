#!/usr/bin/env python
import unittest
from library_app import app, db
from library_app.models import Genre


class GenreModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_to_dict(self):
        genre = Genre(name='test', description='test description').to_dict()
        self.assertEqual(genre['name'], 'test')
        self.assertEqual(genre['description'], 'test description')
        self.assertEqual(genre['unique_books'], 0)
        self.assertEqual(genre['total_copies'], 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

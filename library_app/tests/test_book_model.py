#!/usr/bin/env python
import unittest
from library_app import app, db
from library_app.models import Genre, Book


class GenreModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_genre_to_db(self):
        genre = Genre.query.filter_by(name='test').first()
        self.assertIsNone(genre)
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        genre = Genre.query.get(1)
        self.assertEqual(genre.name, 'test')
        self.assertEqual(genre.description, 'test description')
        self.assertEqual(genre.books, [])
        self.assertNotEqual(genre.name, 'testing')
        self.assertNotEqual(genre.description, 'testing description')
        self.assertNotEqual(genre.books, [1, 2])

    def test_to_dict(self):
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        book = Book(isbn='1-23-456789-X', title='test', author='test author',
                    year=2021, publisher='test publisher', copies=5,
                    genre_id=Genre.query.get(1).id).to_dict()
        self.assertEqual(book['isbn'], '1-23-456789-X')
        self.assertEqual(book['title'], 'test')
        self.assertEqual(book['author'], 'test author')
        self.assertEqual(book['year'], 2021)
        self.assertEqual(book['publisher'], 'test publisher')
        self.assertEqual(book['copies'], 5)
        self.assertEqual(book['genre'], 'test')


    def test_add_book_to_db(self):
        genre = Genre(name='test', description='test description')
        db.session.add(genre)
        db.session.commit()
        book = Book.query.filter_by(isbn='1-23-456789-X').first()
        self.assertIsNone(book)
        with self.assertRaises(AttributeError):
            Book(isbn='1-23-456789-X', title='test',
                 author='test author', year=2021,
                 publisher='test publisher', copies=5,
                 genre_id=Genre.query.get(2).id)
        genre = Genre.query.get(1)
        print(genre)
        book = Book(isbn='1-23-456789-X', title='test',
                    author='test author', year=2021,
                    publisher='test publisher', copies=5,
                    genre_id=Genre.query.filter_by(name='test').first().id)
        db.session.add(book)
        db.session.commit()
        book = Book.query.filter_by(isbn='1-23-456789-X').first()
        self.assertEqual(book.isbn, '1-23-456789-X')
        self.assertEqual(book.title, 'test')
        self.assertEqual(book.author, 'test author')
        self.assertEqual(book.year, 2021)
        self.assertEqual(book.publisher, 'test publisher')
        self.assertEqual(book.copies, 5)
        self.assertEqual(book.genre_id, 1)
        self.assertNotEqual(book.isbn, '2-23-456789-X')
        self.assertNotEqual(book.title, 'testing')
        self.assertNotEqual(book.author, 'test author test')
        self.assertNotEqual(book.year, 2022)
        self.assertNotEqual(book.publisher, 'test publisher test')
        self.assertNotEqual(book.copies, 1)
        self.assertNotEqual(book.genre_id, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
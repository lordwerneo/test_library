from library_app import db
import re

from ..models import Genre, Book


def isbn_checker(isbn):
    """
    Check ISBN for invalid characters, length, format and checksum.
    """
    # Check for invalid characters
    if re.search(r'[\d-]+[0-9X]$', isbn).group() != isbn:
        return 'Invalid characters'
    # Strip of redundant characters
    isbn_filtered = ''.join(re.findall(r'[\dX]+', isbn)) \
        if isbn[-1] == 'X' and len(isbn) == 13 \
        else ''.join(re.findall(r'[\d]+', isbn))
    if len(isbn_filtered) == 10:
        # Check for invalid format
        if isbn.count('-') == 3:
            checksum = 0
            for index, value in enumerate(isbn_filtered[:-1]):
                checksum += int(value) * (10-index)
            checksum = 11 - (checksum % 11)
            if checksum == 11:
                checksum = 0
            elif checksum == 10:
                checksum = 'X'
            # Check for invalid checksum
            if str(checksum) != isbn[-1]:
                return 'Invalid checksum'
        else:
            return 'Invalid format'
    elif len(isbn_filtered) == 13:
        # Check for invalid format
        if isbn.count('-') == 4:
            checksum = 0
            for index, value in enumerate(isbn_filtered[:-1]):
                if index % 2 == 0:
                    checksum += int(value)
                else:
                    checksum += 3 * int(value)
            checksum = 10 - checksum % 10
            if str(checksum) != isbn[-1]:
                return 'Invalid checksum'
        else:
            return 'Invalid format'
    else:
        return 'Invalid length'
    return None


def get_all_books():
    books = Book.query.all()
    if books:
        return [book.to_dict() for book in books]
    return 'Error'


def get_genre_books(genre):
    genre = Genre.query.filter_by(name=genre).first()
    if not genre:
        return 'No genre'
    books = Book.query.filter_by(genre_id=genre.id).all()
    if books:
        return [book.to_dict() for book in books]
    return 'Error'


def get_filtered_books(year_start, year_end, genre):
    books = Book.query
    if year_start:
        books = books.filter(Book.year >= int(year_start))
    if year_end:
        books = books.filter(Book.year <= int(year_end))
    if int(genre) > 0:
        books = books.filter(Book.genre_id == int(genre))
    books = [book.to_dict() for book in books]
    return books


def post_book(isbn, title, author, year, publisher, copies, genre):
    genre_id = Genre.query.filter_by(name=genre).first()
    book = Book.query.filter_by(isbn=isbn).first()
    if genre_id:
        if not book:
            book = Book(isbn=isbn, title=title, author=author, year=year,
                        publisher=publisher, copies=copies,
                        genre_id=genre_id.id)
            db.session.add(book)
            db.session.commit()
            return
        return 'ISBN exists'
    return 'No genre'


def put_book(cur_isbn, isbn, title, author, year, publisher, copies, genre):
    genre_id = Genre.query.filter_by(name=genre).first()
    if genre_id:
        book = Book.query.filter_by(isbn=cur_isbn).first()
        if not book:
            new_book = Book.query.filter_by(isbn=isbn).first()
            if not new_book:
                new_book = Book(isbn=isbn, title=title, author=author,
                                year=year, publisher=publisher, copies=copies,
                                genre_id=genre_id.id)
                db.session.add(new_book)
                db.session.commit()
                return
            return 'ISBN exists'
        book.title = title
        book.author = author
        book.year = year
        book.publisher = publisher
        book.copies = copies
        book.genre_id = genre_id.id
        db.session.commit()
        return 'Updated'
    return 'No genre'


def delete_book(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if not book:
        return 'Error'
    db.session.delete(book)
    db.session.commit()


def get_book_by_isbn(isbn):
    book = Book.query.filter_by(isbn=isbn).first()
    if book:
        return book.to_dict()
    return 'Error'


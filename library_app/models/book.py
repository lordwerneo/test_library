from library_app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    title = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    publisher = db.Column(db.String(64), nullable=False)
    copies = db.Column(db.Integer, nullable=False, default=1)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    def __repr__(self):
        return f'Book({self.isbn}, {self.title}, {self.author}, ' \
               f'{self.year}, {self.publisher}, {self.copies})'

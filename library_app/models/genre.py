from library_app import db


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    books = db.relationship('Book', cascade="all,delete",
                            backref='genre', lazy=True)

    def __repr__(self):
        return f'Genre({self.name}, {self.description}).'


    def to_dict(self):
        """

        :return:
        """
        return {
            'name': self.name,
            'description': self.description,
            'unique_books': len(self.books),
            'total_copies': sum([book.copies for book in self.books])
        }

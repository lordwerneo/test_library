import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, \
    NumberRange
from library_app.models import Book, Genre
from library_app.service.book_service import isbn_checker


# def isbn_checker(isbn):
#     """
#     Check ISBN for invalid characters, length, format and checksum.
#     """
#     # Check for invalid characters
#     if re.search(r'[\d-]+[0-9X]$', isbn).group() != isbn:
#         return 'Invalid characters'
#     # Strip of redundant characters
#     isbn_filtered = ''.join(re.findall(r'[\dX]+', isbn)) \
#         if isbn[-1] == 'X' and len(isbn) == 13 \
#         else ''.join(re.findall(r'[\d]+', isbn))
#     if len(isbn_filtered) == 10:
#         # Check for invalid format
#         if isbn.count('-') == 3:
#             checksum = 0
#             for index, value in enumerate(isbn_filtered[:-1]):
#                 checksum += int(value) * (10-index)
#             checksum = 11 - (checksum % 11)
#             if checksum == 11:
#                 checksum = 0
#             elif checksum == 10:
#                 checksum = 'X'
#             # Check for invalid checksum
#             if str(checksum) != isbn[-1]:
#                 return 'Invalid checksum'
#         else:
#             return 'Invalid format'
#     elif len(isbn_filtered) == 13:
#         # Check for invalid format
#         if isbn.count('-') == 4:
#             checksum = 0
#             for index, value in enumerate(isbn_filtered[:-1]):
#                 if index % 2 == 0:
#                     checksum += int(value)
#                 else:
#                     checksum += 3 * int(value)
#             checksum = 10 - checksum % 10
#             if str(checksum) != isbn[-1]:
#                 return 'Invalid checksum'
#         else:
#             return 'Invalid format'
#     else:
#         return 'Invalid length'
#     return None


class AddBookForm(FlaskForm):
    isbn = StringField('ISBN',
                       validators=[DataRequired(), Length(min=10, max=20)])
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=1, max=64)])
    author = StringField('Author',
                         validators=[DataRequired(), Length(min=1, max=64)])
    year = IntegerField(
        'Year',
        validators=[DataRequired(),
                    NumberRange(min=1900, max=2022,
                                message='Year should be from 1900 to 2022')])
    publisher = StringField('Publisher',
                            validators=[DataRequired(), Length(min=1, max=64)])
    copies = IntegerField(
        'Copies',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=999,
                        message='Books copies should be from 1 to 999')])
    genre = SelectField('Genre', choices=[], validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_isbn(self, isbn):
        isbn_db = Book.query.filter_by(isbn=isbn.data).first()
        if isbn_db:
            raise ValidationError(f'ISBN {isbn.data} already exists.')
        check_status = isbn_checker(isbn.data)
        if check_status:
            raise ValidationError(f'ISBN {isbn.data} {check_status}.')


class UpdateBookForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=1, max=64)])
    author = StringField('Author',
                         validators=[DataRequired(), Length(min=1, max=64)])
    year = IntegerField(
        'Year',
        validators=[DataRequired(),
                    NumberRange(min=1900, max=2022,
                                message='Year should be from 1900 to 2022')])
    publisher = StringField('Publisher',
                            validators=[DataRequired(), Length(min=1, max=64)])
    copies = IntegerField(
        'Copies',
        validators=[
            DataRequired(),
            NumberRange(min=1, max=999,
                        message='Books copies should be from 1 to 999')])
    genre = SelectField('Genre', choices=[], validators=[DataRequired()])
    submit = SubmitField('Update')


class FilterBookForm(FlaskForm):
    message = 'Year should be from 1900 to 2022'
    year_start = IntegerField('From', default=1900,
                              validators=[NumberRange(min=1900, max=2022,
                                                      message=message)])
    year_end = IntegerField('To', default=2022,
                            validators=[NumberRange(min=1900, max=2022,
                                                    message=message)])
    genre = SelectField('Genre', choices=[])
    submit = SubmitField('Search')

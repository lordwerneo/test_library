from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from library_app.models import Genre


class AddGenreForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=1, max=20)])
    description = StringField('Description',
                              validators=[DataRequired(),
                                          Length(min=1, max=255)])
    submit = SubmitField('Submit')

    def validate_name(self, name):
        name_db = Genre.query.filter_by(name=name.data.lower()).first()
        if name_db:
            raise ValidationError(f'Genre "{name.data}" already exists.')
        if not name.data.isalpha():
            raise ValidationError(f'Genre should contain only letters.')


class UpdateGenreForm(AddGenreForm):
    submit = SubmitField('Update')

    def __init__(self, original_name, *args, **kwargs):
        super(UpdateGenreForm, self).__init__(*args, **kwargs)
        self.original_name = original_name

    def validate_name(self, name):
        name_db = Genre.query.filter_by(name=name.data.lower()).first()
        if name_db and name.data != self.original_name:
            raise ValidationError(f'Genre "{name.data}" already exists.')
        if not name.data.isalpha():
            raise ValidationError(f'Genre should contain only letters.')

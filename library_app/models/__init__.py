"""
__init__.py file of models module with imported genre and book submodules
"""

from . import genre
from . import book

Genre = genre.Genre
Book = book.Book

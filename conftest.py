import pytest

from data import book_names, genre_names
from main import BooksCollector


@pytest.fixture()
def collector():
    return BooksCollector()

@pytest.fixture()
def add_book_to_library(collector):
    for i in book_names:
        collector.add_new_book(i)
    return collector

@pytest.fixture()
def add_book_to_library_with_genre(add_book_to_library):
    for i in range(len(book_names)):
        add_book_to_library.set_book_genre(book_names[i], genre_names[i])
    return add_book_to_library

@pytest.fixture()
def add_book_to_list_of_favorites_books(add_book_to_library):
    for i in book_names:
        add_book_to_library.add_book_in_favorites(i)
    return add_book_to_library



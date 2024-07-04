import pytest

from data import default_state_book_collector, book_bad_names, test_params


class TestBooksCollector:

    # проверка создания объекта первоначального состояния параметров объекта класса
    @pytest.mark.parametrize('argument, state', default_state_book_collector)
    def test_default_argument_state(self, argument, state, collector):
        assert getattr(collector, argument) == state

    # проверка на добавление книг в коллекцию
    def test_add_new_books_three_books(self, add_book_to_library):

        assert len(add_book_to_library.books_genre) == 3

    # проверка на добавление книги с недопустимой длинной названия и на повторное добавление фильма в библиотеку
    @pytest.mark.parametrize('bad_name', book_bad_names)
    def test_add_bad_name_books_library_is_empty(self, bad_name, collector):
        collector.add_new_book(bad_name)
        assert len(collector.books_genre) == 0

    # проверка на установку жанра ранее добавленной книги
    @pytest.mark.parametrize(
        'name, genre, result', [
            ('Гордость и предубеждение и зомби', 'Ужасы', 'Ужасы'),
            ('Что делать, если ваш кот хочет вас убить', 'Пародия', '')
        ]
    )
    def test_set_book_genre_success(self, name, genre, result, add_book_to_library):
        add_book_to_library.set_book_genre(name, genre)
        assert add_book_to_library.books_genre[name] == result

    # проверка получения жанра книги по её имени
    @pytest.mark.parametrize('name, genre', test_params)
    def test_get_book_genre_success(self, name, genre, add_book_to_library_with_genre):
        assert add_book_to_library_with_genre.get_book_genre(name) == genre

    # проверка вывода списока книг с определённым жанром
    def test_books_with_specific_genre_success(self, add_book_to_library_with_genre):
        assert add_book_to_library_with_genre.get_books_with_specific_genre('Комедии') == ['Как я встретил вашу маму']

    # проверка получение словаря books_genre
    def test_get_books_genre_three_books(self, add_book_to_library):
        assert len(add_book_to_library.get_books_genre()) == 3

    # проверка возвращения списка книг, подходящие детям
    def test_get_books_for_children_one_book(self, add_book_to_library_with_genre):
        assert add_book_to_library_with_genre.get_books_for_children() == ['Как я встретил вашу маму']

    # проверка добавления книги в Избранное
    @pytest.mark.parametrize(
        'name, result',
        [
            ('Гордость и предубеждение и зомби', 1),
            ('', 0)
         ]
    )
    def test_add_book_in_favorites(self, name, result, add_book_to_library):
        add_book_to_library.add_book_in_favorites(name)
        assert len(add_book_to_library.favorites) == result

    # проверка на удаление книги из Избранного
    def test_delete_book_from_favorites_success(self, add_book_to_list_of_favorites_books):
        add_book_to_list_of_favorites_books.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(add_book_to_list_of_favorites_books.favorites) == 2

    # проверка на получение списка Избранных книг
    def test_get_list_of_favorites_books(self, add_book_to_list_of_favorites_books):
        assert len(add_book_to_list_of_favorites_books.get_list_of_favorites_books()) == 3

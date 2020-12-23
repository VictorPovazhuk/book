"""Compare ratings for film and book"""

import time
from pprint import pprint
import films_reader
import books_reader


def get_film_rating(title):
    title_basics = films_reader.get_tt_basics(title)
    if not title_basics:
        return None

    tconst = title_basics[0]
    genres = title_basics[8].split(',')

    writer_basics = films_reader.get_tt_writer(tconst)
    if not writer_basics:
        return None

    rate = films_reader.get_tt_rating(tconst)

    return rate


def get_book_rating(title):
    gb_rate = books_reader.get_gb_rating(title)
    bc_rate = books_reader.get_bc_rating(title)

    rates = [rate for rate in [gb_rate, bc_rate]
             if rate > 0]

    if len(rates) > 0:
        return sum(rates) / len(rates)
    return None


def compare(film_title, book_title):
    film_rate = get_film_rating(film_title)
    book_rate = get_book_rating(book_title)

    return (film_rate, book_rate)


def test_funcs():
    film_title = 'Don Juan DeMarco'
    book_title = 'Don Juan (Penguin Classics)'
    comp = compare(film_title, book_title)
    print(
        f'Film {film_title}: {comp[0]} / 10,\nBook {book_title}: {comp[1]} / 5')


if __name__ == '__main__':
    start = time.time()
    test_funcs()
    print(time.time() - start)

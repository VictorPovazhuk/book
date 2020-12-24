"""Compare ratings for film and book"""

import films_reader
import books_reader


def get_film_rating(title: str) -> float:
    '''
    Return film rating
    >>> get_film_rating('Don Juan DeMarco')
    6.7
    '''
    title_basics = films_reader.get_tt_basics(title)
    if not title_basics:
        return None

    tconst = title_basics[0]

    writer_basics = films_reader.get_tt_writer(tconst)
    if not writer_basics:
        return None

    rate = films_reader.get_tt_rating(tconst)

    return rate


def get_book_rating(title: str) -> float:
    '''
    Return book rating
    >>> get_book_rating('Don Juan (Penguin Classics)')
    4.5
    '''
    gb_rate = books_reader.get_gb_rating(title)
    bc_rate = books_reader.get_bc_rating(title)

    rates = [rate for rate in [gb_rate, bc_rate]
             if rate > 0]

    if len(rates) > 0:
        return sum(rates) / len(rates)
    return None


def compare(film_title: str, book_title: str) -> tuple:
    '''
    Return film and book rating in comparison
    >>> compare('Don Juan DeMarco', 'Don Juan (Penguin Classics)')
    (6.7, 4.5)
    >>> compare('Quick fly', 'Don Juan (Penguin Classics)')
    (None, 4.5)
    '''
    film_rate = get_film_rating(film_title)
    book_rate = get_book_rating(book_title)

    return (film_rate, book_rate)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
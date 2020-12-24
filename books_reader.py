'''Work with books dbs'''

import pandas as pd
import os

BOOKS_DATA_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'DATA')


def load_bnl_books():
    '''
    Return BN Library overview database
    '''
    df = pd.read_csv(os.path.join(BOOKS_DATA_DIR, 'bnl/records.csv'))
    return df


def get_gb_rating(title: str) -> float:
    '''
    Return book rating from GoodReads database
    >>> get_gb_rating('To Kill a Mockingbird') == 4.25
    True
    '''
    df = pd.read_csv(os.path.join(BOOKS_DATA_DIR, 'goodbooks_10k/books.csv'))
    rates = df.average_rating[df['original_title'] == title]
    if len(rates) > 0:
        rate = rates.iloc[0]
        return rate
    else:
        return 0


def get_bc_rating(title: str) -> float:
    '''
    Return book rating from Books-Crossing database
    >>> get_bc_rating("The Mummies of Urumchi") == 0
    True
    >>> get_bc_rating("The Testament") == 3.85
    True
    '''
    df = pd.read_csv(os.path.join(BOOKS_DATA_DIR, 'book_crossing/books.csv'),
                     sep=';', escapechar='\\')
    isbn = df[df['Book-Title'] == title]['ISBN']
    if len(isbn) > 0:
        isbn = isbn.iloc[0]
    else:
        return 0

    df = pd.read_csv(os.path.join(BOOKS_DATA_DIR, 'book_crossing/ratings.csv'),
                     sep=';', escapechar='\\')
    rates = df[(df['ISBN'] == isbn) & (df['Book-Rating'] > 0)]['Book-Rating']
    if len(rates) > 0:
        rate = round((rates.sum() / len(rates)) / 2, 2)
        return rate
    else:
        return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''Work with books dbs'''

import pandas as pd
import os

BOOKS_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'DATA')

def get_gb_rating(title):
    df = pd.read_csv(os.path.join(BOOKS_DATA_DIR, 'goodbooks_10k/books.csv'))
    rates = df.average_rating[df['original_title'] == title]
    if len(rates) > 0:
        rate = rates.iloc[0]
        return rate
    else:
        return 0

def get_bc_rating(title):
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
        rate = (rates.sum() / len(rates)) / 2
        return rate
    else:
        return 0
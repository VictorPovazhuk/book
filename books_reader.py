'''Work with books dbs'''

import pandas as pd

def get_gb_rating(title):
    df = pd.read_csv('DATA/library/goodbooks_10k/books.csv')
    rates = df.average_rating[df['original_title'] == title]
    if len(rates) > 0:
        rate = rates.iloc[0]
        return rate
    else:
        return 0

def get_bc_rating(title):
    df = pd.read_csv('DATA/library/book_crossing/books.csv',
                     sep=';', escapechar='\\')
    isbn = df[df['Book-Title'] == title]['ISBN']
    if len(isbn) > 0:
        isbn = isbn.iloc[0]
    else:
        return 0

    df = pd.read_csv('DATA/library/book_crossing/ratings.csv',
                     sep=';', escapechar='\\')
    rates = df[(df['ISBN'] == isbn) & (df['Book-Rating'] > 0)]['Book-Rating']
    if len(rates) > 0:
        rate = (rates.sum() / len(rates)) / 2
        return rate
    else:
        return 0
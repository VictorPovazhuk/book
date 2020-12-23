"""Compare reviews for films and book"""

import time
from pprint import pprint
import pandas as pd
import csv

# def get_few_titles():
#     with open('DATA/cinema/title.basics.tsv') as f:
#         titles = []
#         for i in range(10):
#             titles.append(f.readline())
#     return titles


def get_title_rating(tconst):
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if (info[0] == tconst):
                return (float(info[1]), int(info[2]))
    return None


def get_title_writer(tconst):
    with open('DATA/cinema/title.principals.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if info[0] == tconst and info[3] == 'writer':  # 'Don Juan' in info[4] and #
                return info
    return None


def get_title_basics(title):
    with open('DATA/cinema/title.basics.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if info[3] == title:
                return info
    return None


def test_film():
    title_basics = get_title_basics('Don Juan DeMarco')

    tconst = title_basics[0]
    genres = title_basics[8].split(',')

    writer_basics = get_title_writer(tconst)

    if writer_basics != None:
        rate, num_votes = get_title_rating(tconst)

    pprint(rate)


def main():
    book_name = "Don Juan (Penguin Classics)"
    book_rate = get_book_rating(book_name)
    print(book_rate)


def get_book_rating(title):
    df = pd.read_csv('DATA/library/goodbooks_10k/books.csv')
    rates = df.average_rating[df['original_title'] == title]
    if len(rates) > 0:
        print('GoodBook!')
        rate = rates.iloc[0]
        return rate

    df = pd.read_csv('DATA/library/book_crossing/books.csv',
                     sep=';', escapechar='\\')
    # "Don Juan (Penguin Classics)";"George Gordon Byron, Baron Byron"
    isbn = df[df['Book-Title'] == title]['ISBN']
    if len(isbn) > 0:
        isbn = isbn.iloc[0]
    else:
        return None

    df = pd.read_csv('DATA/library/book_crossing/ratings.csv',
                     sep=';', escapechar='\\')
    rates = df[(df['ISBN'] == isbn) & (df['Book-Rating'] > 0)]['Book-Rating']
    if len(rates) > 0:
        print('BookCrossing!')
        rate = (rates.sum() / len(rates)) / 2
        return rate
    else:
        return None


def test_book():
    book_name = "Don Juan (Penguin Classics)"
    author = 'Lord Byron'
    book_rate = get_book_rating(book_name)
    print(book_rate)


if __name__ == '__main__':
    start = time.time()
    test_film()
    print(time.time() - start)

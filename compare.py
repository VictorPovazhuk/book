"""Compare reviews for films and book"""

import time
from pprint import pprint
import pandas as pd
import csv


# def get_title_ratings(title_ids):
#     rates = {}
#     cp_ids = title_ids.copy()
#     with open('DATA/cinema/title.ratings.tsv') as f:
#         for line in iter(f.readline, ''):
#             info = line.strip().split('\t')
#             if (info[0] in cp_ids):
#                 rates[info[0]] = (float(info[1]), int(info[2]))
#                 cp_ids.remove(info[0])
#     return rates

# is each film that has appropriate title based on the book ? ->
# need to know author of the book to find appropriate film


# def get_title_ids(title, person_ids):
#     title_ids = []
#     cp_person_ids = person_ids.copy()
#     with open('DATA/cinema/title.akas.tsv') as f:
#         for line in iter(f.readline, ''):
#             info = line.strip().split('\t')
#             if (info[2] == title) and (info[0] in cp_person_ids):
#                 title_ids.append(info[0])
#                 cp_person_ids.remove(info[0])
#     return title_ids


# def get_person_titles_ids(writer):
#     ids = []
#     with open('DATA/cinema/title.crew.tsv') as f:
#         for line in iter(f.readline, ''):
#             info = line.strip().split('\t')
#             writers = info[2].split(',')
#             if writer in writers:
#                 ids.append(info[0])
#     return ids


# def get_film_writer(author):
#     with open('DATA/cinema/name.basics.tsv') as f:
#         for line in iter(f.readline, ''):
#             info = line.strip().split('\t')
#             if info[1] == author:
#                 return info[0]

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

# def get_titles():
#     with open('DATA/cinema/title.basics.tsv') as f:
#         titles = []
#         for i in range(10):
#             titles.append(f.readline())
#     return titles


def get_title_basics(title):
    with open('DATA/cinema/title.basics.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if info[3] == title:
                return info
    return None


def test_film():
    # book_name = 'Don Juan'
    # writer = 'nm0126406'
    # person_titles_ids = ['tt0016804', 'tt3213496', 'tt0003795']
    # t_ids = ['tt0016804', 'tt3213496']
    # f_rates = {'tt0016804': (7.0, 739)}
    # tts = get_titles()
    # pprint(tts)
    title_basics = get_title_basics('Don Juan DeMarco')

    tconst = title_basics[0]
    genres = title_basics[8].split(',')

    writer_basics = get_title_writer(tconst)

    if writer_basics != None:
        rate, num_votes = get_title_rating(tconst)

    pprint(rate)


def main():
    book_name = 'Don Juan'
    # author = 'Lord Byron'
    # writer = get_film_writer(author)
    # print(writer)
    # person_titles_ids = get_person_titles_ids(writer)
    # print(person_titles_ids)
    # title_ids = get_title_ids(book_name, person_titles_ids)
    # pprint(title_ids)
    # film_rates = get_title_ratings(title_ids)
    # pprint(film_rates)
    book_name = "Don Juan (Penguin Classics)"
    author = 'Lord Byron'
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

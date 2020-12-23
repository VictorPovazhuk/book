"""Compare reviews for films and book"""

import time
from pprint import pprint
import pandas as pd
import csv


def get_title_ratings(title_ids):
    rates = {}
    cp_ids = title_ids.copy()
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if (info[0] in cp_ids):
                rates[info[0]] = (float(info[1]), int(info[2]))
                cp_ids.remove(info[0])
    return rates

# is each film that has appropriate title based on the book ? ->
# need to know author of the book to find appropriate film


def get_title_ids(title, person_ids):
    title_ids = []
    cp_person_ids = person_ids.copy()
    with open('DATA/cinema/title.akas.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if (info[2] == title) and (info[0] in cp_person_ids):
                title_ids.append(info[0])
                cp_person_ids.remove(info[0])
    return title_ids


def get_person_titles_ids(writer):
    ids = []
    with open('DATA/cinema/title.crew.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            writers = info[2].split(',')
            if writer in writers:
                ids.append(info[0])
    return ids


def get_film_writer(author):
    with open('DATA/cinema/name.basics.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if info[1] == author:
                return info[0]


def main():
    book_name = 'Don Juan'
    author = 'Lord Byron'
    writer = get_film_writer(author)
    print(writer)
    person_titles_ids = get_person_titles_ids(writer)
    print(person_titles_ids)
    title_ids = get_title_ids(book_name, person_titles_ids)
    pprint(title_ids)
    film_rates = get_title_ratings(title_ids)
    pprint(film_rates)


def test_film():
    book_name = 'Don Juan'
    writer = 'nm0126406'
    person_titles_ids = ['tt0016804', 'tt3213496', 'tt0003795']
    t_ids = ['tt0016804', 'tt3213496']
    f_rates = {'tt0016804': (7.0, 739)}


def get_book_rating(title):
    with open('DATA/library/goodbooks_10k/books.csv') as f:
        i = 0
        for line in iter(f.readline, ''):
            info = line.strip().split(',')
            if i < 3:
                for n in range(len(info)):
                    print(str(n) + str(info[n]))
            i += 1
            # and (info[0] in cp_person_ids): # f'"{title}"'
            if (title in info[10]):
                return float(info[12]), int(info[13])
                # books.append(info[0])
    return None

def get_book_rating_1():
    df = pd.read_csv('DATA/library/goodbooks_10k/books.csv')
    pprint(list(df.title[df['average_rating'] > 4.7]))

# def get_book_rating_2():
#     with open('DATA/library/goodbooks_10k/books.csv') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#             #     # print(f'Column names are {", ".join(row)}')
#             #     # pprint(list(enumerate(row)))
#                 line_count += 1
#             # else:
#                 # print(f'\t{", ".join(row)}')
#             elif float(row[12]) > 4.7:
#                 # print(row[10], row[12])
#                 0
#             line_count += 1
#             # if line_count > 2:
#             #     break
#         # print(f'Processed {line_count} lines.')


# missed the decription file 'under my nose' -> should be attentive
# check if book with similar title exsts at all


# def get_book_id(title, author):
#     books = []
#     with open('DATA/library/bnb/titles.csv') as f:
#         for line in iter(f.readline, ''):
#             info = [piece.strip('"') for piece in line.strip().split(',')]
#             if (title in info[0]):  # and (info[0] in cp_person_ids):
#                 books.append(info[0])
#     return books


def test_book():
    book_name = 'The Hunger Games (The Hunger Games, #1)'
    author = 'Lord Byron'
    # book_id = get_book_id(book_name, author)
    # print(book_id)
    # rate = get_book_rating(book_name)
    # print(rate)
    get_book_rating_2()


if __name__ == '__main__':
    start = time.time()
    get_book_rating_1()
    print(time.time() - start)
    start = time.time()
    get_book_rating_2()
    print(time.time() - start)

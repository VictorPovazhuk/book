"""Compare reviews for film and book"""

import time
from pprint import pprint


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

# def get_film_ratings(title_ids):
#     infos = []
#     cp_ids = title_ids.copy()
#     with open('DATA/cinema/title.ratings.tsv') as f:
#         for line in iter(f.readline, ''):
#             info = line.strip().split('\t')
#             if (info[0] in cp_ids):
#                 infos.append(info)
#                 cp_ids.remove(info[0])
#     return infos

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


def get_author(title):
    return 'Lord Byron'


def get_film_writer(author):
    with open('DATA/cinema/name.basics.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if info[1] == author:
                return info[0]


def main():
    book_name = 'Don Juan'
    author = get_author(book_name)
    writer = get_film_writer(author)
    print(writer)
    person_titles_ids = get_person_titles_ids(writer)
    print(person_titles_ids)
    title_ids = get_title_ids(book_name, person_titles_ids)
    pprint(title_ids)
    film_rates = get_title_ratings(title_ids)
    pprint(film_rates)


def test():
    book_name = 'Don Juan'
    writer = 'nm0126406'
    person_titles_ids = ['tt0016804', 'tt3213496', 'tt0003795']
    t_ids = ['tt0016804', 'tt3213496']
    rates = {'tt0016804': (7.0, 739)}


if __name__ == '__main__':
    start = time.time()
    # test()
    main()
    print(time.time() - start)

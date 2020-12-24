'''Work with fims db'''

# def get_few_titles():
#     with open('DATA/cinema/title.basics.tsv') as f:
#         titles = []
#         for i in range(10):
#             titles.append(f.readline())
#     return titles

import os

FILMS_DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'DATA/imdb')

def get_tt_rating(tconst):
    with open(os.path.join(FILMS_DATA_DIR, 'title.ratings.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if (info[0] == tconst):
                return float(info[1])
    return None


def get_tt_writer(tconst):
    with open(os.path.join(FILMS_DATA_DIR, 'title.principals.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if info[0] == tconst and info[3] == 'writer':
                return info
    return None


def get_tt_basics(title):
    with open(os.path.join(FILMS_DATA_DIR, 'title.basics.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if info[3] == title:
                return info
    return None

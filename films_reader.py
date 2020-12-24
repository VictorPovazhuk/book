'''Work with fims db'''

import os

FILMS_DATA_DIR = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'DATA/imdb')


def get_tt_rating(tconst: str) -> float:
    '''
    Return film rating
    >>> get_tt_rating('tt0000015')
    6.1
    >>> get_tt_rating('tt00')
    '''
    with open(os.path.join(FILMS_DATA_DIR, 'title.ratings.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if (info[0] == tconst):
                return float(info[1])
    return None


def get_tt_writer(tconst: str) -> list:
    '''
    Return info about film writer
    >>> get_tt_writer('tt0000015') == None
    True
    '''
    with open(os.path.join(FILMS_DATA_DIR, 'title.principals.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if info[0] == tconst and info[3] == 'writer':
                return info
    return None


def get_tt_basics(title: str) -> list:
    '''
    Return basic info about film
    >>> get_tt_basics('The Clown Barber')[0] == 'tt0000019'
    True
    '''
    with open(os.path.join(FILMS_DATA_DIR, 'title.basics.tsv')) as f:
        for line in f:
            info = line.strip().split('\t')
            if info[3] == title:
                return info
    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()

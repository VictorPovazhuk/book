"""Compare reviews for film and book"""

import time
from pprint import pprint


def get_film_rating(title_id):
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if (info[0] == title_id):
                return float(info[1]), int(info[2])
    return None


def get_title_id(title):
    infos = []
    with open('DATA/cinema/title.akas.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if (info[2] == title) and (int(info[7]) == 1):
                infos.append(info)
    return infos


def main():
    # title_id = 'tt0016804'
    title_ids = get_title_id('Don Juan')
    pprint(title_ids)
    # rate = get_film_rating(title_id)
    # print(rate)


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)

'''Work with fims db'''

# def get_few_titles():
#     with open('DATA/cinema/title.basics.tsv') as f:
#         titles = []
#         for i in range(10):
#             titles.append(f.readline())
#     return titles

def get_tt_rating(tconst):
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if (info[0] == tconst):
                return float(info[1])
    return None


def get_tt_writer(tconst):
    with open('DATA/cinema/title.principals.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if info[0] == tconst and info[3] == 'writer':
                return info
    return None


def get_tt_basics(title):
    with open('DATA/cinema/title.basics.tsv') as f:
        for line in f:
            info = line.strip().split('\t')
            if info[3] == title:
                return info
    return None

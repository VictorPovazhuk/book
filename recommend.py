'''Recommend some books'''

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer
import os
import books_reader


def remove_punctuation(text: str) -> str:
    '''
    Return cleaned string
    >>> remove_punctuation('Very, long, sentence')
    'Very long sentence'
    '''
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text


def get_recommend_title(df: pd.DataFrame, title: str) -> list:
    '''
    Return books recommended by title
    '''
    data = df.copy(deep=True)

    # create cleaned titles to calculate cosine similarity
    data['format_title'] = data['Title'].str.lower()
    data['format_title'] = data['format_title'].apply(func=remove_punctuation)
    data.drop_duplicates(subset='format_title', keep='first', inplace=True)

    # create new indices for interacting between dataframe and matrix
    data.reset_index(level=0, inplace=True)

    idx = data.index[data['Title'] == title][0]

    tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2),
                         min_df=1, stop_words='english')
    tfidf_matrix = tf.fit_transform(data['format_title'])

    # get matrix for specified title
    tt_matrix = tfidf_matrix[idx]

    sim_arr = cosine_similarity(tt_matrix, tfidf_matrix)[0]

    # enumerate array elements to correspond books indices in data
    idx_sim = list(enumerate(sim_arr))

    idx_sim = sorted(idx_sim, key=lambda x: x[1], reverse=True)
    idx_sim = idx_sim[1:6]

    recoms = [(data['Title'].iloc[el[0]], el[1]) for el in idx_sim]

    return recoms


def recommend_books(title: str, genre: str) -> list:
    '''
    Return recommended other books
    >>> recommend_books('Don Juan Demarico', 'Romance')[3] == 'Byron, Don Juan'
    True
    >>> recommend_books('The Shelley-Byron men : lost angels of\
a ruined paradise', 'Biography')[2]
    'Shelley and Byron in Pisa'
    '''
    df = books_reader.load_bnl_books()

    # filtrate titles
    df = df[df['Title'].notnull()]

    # add specified title
    df3 = pd.DataFrame([[title, genre]], columns=['Title', 'Genre'])
    df2 = df.append(df3)

    no_genre_recoms = get_recommend_title(df2, title)

    df2 = df2[df2['Genre'].notnull()]
    df2 = df2[df2['Genre'].str.contains(genre)]
    genre_recoms = get_recommend_title(df2, title)

    recoms = []
    i1 = i2 = 0
    for _ in range(5):
        if genre_recoms[i1][1] < 0.15 and no_genre_recoms[i2][1] > 0.1:
            recoms.append(no_genre_recoms[i2][0])
            i2 += 1
        else:
            recoms.append(genre_recoms[i1][0])
            i1 += 1

    return recoms


if __name__ == '__main__':
    import doctest
    doctest.testmod()

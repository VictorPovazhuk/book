import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer


def remove_punctuation(text):
    tokenizer = RegexpTokenizer(r'\w+')
    text = tokenizer.tokenize(text)
    text = " ".join(text)
    return text


def recommend_title(title, genre):
    df = pd.read_csv('DATA/library/bnb/records.csv')

    # filtrate genre
    df2 = df[df['Genre'].notnull()]

    # add specified title
    df3 = pd.DataFrame([[title, genre]], columns=['Title', 'Genre'])
    df2 = df2.append(df3)

    data = df2[df2['Genre'].str.contains(genre)]
    print(data)

    # create cleaned titles to calculate cosine similarity
    df2['format_title'] = df2['Title'].str.lower()
    df2['format_title'] = df2['format_title'].apply(func=remove_punctuation)
    df2.drop_duplicates(subset='format_title', keep='first', inplace=True)

    # create new indices for interacting in all data frames
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

    book_indices = [i[0] for i in idx_sim]
    recommends = data['Title'].iloc[book_indices]

    return recommends


def test_funcs():
    title, genre = 'The Shelley-Byron men : lost angels of a ruined paradise', 'Drama'
    recs = recommend_title(title, genre)
    print(list(recs))


if __name__ == '__main__':
    test_funcs()

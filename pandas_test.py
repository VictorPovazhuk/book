import pandas as pd
import time

def read_pandas_1():
    df = pd.read_csv('DATA/cinema/title.akas.tsv', sep='\t',
                    dtype={'titleId': 'string', 'ordering': int,
                            'title': 'string', 'region': 'string',
                            'language': 'string', 'types': 'string',
                            'attributes': 'string',
                            'isOriginalTitle': 'string'})
    print(df.head())

def read_pandas_2():
    # df = pd.DataFrame(columns=['id', 'rating', 'votes'])
    ratings = {'id': [], 'rating': [], 'votes': []}
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            keys = list(ratings.keys())
            if (info[0] == 'tt0016804'):
                for i in range(len(info)):
                    ratings[keys[i]].append(info[i])
                # print('!!!' + str(info))
                # df2 = pd.DataFrame([info], columns=['id', 'rating', 'votes'])
                # print(df2)
                # df = df.append(df2)
                # print(df)
    df = pd.DataFrame(ratings, index=[i for i in range(len(ratings['id']))])
    return df

def read_pandas_3():
    ratings = []
    with open('DATA/cinema/title.ratings.tsv') as f:
        for line in iter(f.readline, ''):
            info = line.strip().split('\t')
            if info[0] == 'tt0016804':
                info[1], info[2] = float(info[1]), int(info[2])
                ratings.append(info)
    df = pd.DataFrame(ratings, columns=['id', 'rating', 'votes'])
    return df

if __name__ == '__main__':
    # start = time.time()
    # dframe = read_pandas_2()
    # print(time.time() - start)
    start = time.time()
    dframe = read_pandas_3()
    print(time.time() - start)
    print(dframe['votes'])
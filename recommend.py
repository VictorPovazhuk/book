import pandas as pd

def load_books():
    df = pd.read_csv('DATA/library/bnb/records.csv')
    return df

def test():
    df = load_books()
    print(df.head())

if __name__ == '__main__':
    test()

def data():

    import pandas as pd

    df = pd.read_csv('data/data_noformulas.csv')
    df['Date'] = pd.to_datetime(df['Date'])

    return df
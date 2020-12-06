import pandas as pd


def load_data(path):
    # Load the data
    tweets_df = pd.read_csv(path)
    tweets_df.info()

    # Drop unnecessary cols
    tweets_df = tweets_df.drop(['id'], axis=1)

    return tweets_df

from sklearn.feature_extraction.text import CountVectorizer

from data_preprocessor import message_cleaning


# Define the cleaning pipeline we defined earlier
def Vectorizer(tweets_df):
    tweets_countvectorizer = CountVectorizer(analyzer=message_cleaning, dtype='uint8').fit_transform(tweets_df['tweet']).toarray()
    return tweets_countvectorizer

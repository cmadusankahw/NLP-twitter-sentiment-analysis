from data_loader import load_data
from data_preprocessor import message_cleaning
from vectorizer import Vectorizer
import  pandas as pd

tweets_df = load_data("../data/twitter.csv")

# Let's test the newly added function
tweets_df_clean = tweets_df['tweet'].apply(message_cleaning)

print(tweets_df_clean[5]) # show the cleaned up version

print(tweets_df['tweet'][5]) # show the original version

# Vectorize the tweets using tokenizer
tweets_countvectorizer = Vectorizer(tweets_df)

print(tweets_countvectorizer)
print(tweets_countvectorizer.shape)

# dataframe to train
tweets = pd.DataFrame(tweets_countvectorizer)

X = tweets
Y = tweets_df['label']
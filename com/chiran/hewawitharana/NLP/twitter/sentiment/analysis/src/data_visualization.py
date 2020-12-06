import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from data_loader import load_data

tweets_df = load_data("../data/twitter.csv")

sns.heatmap(tweets_df.isnull(), yticklabels=False, cbar=False, cmap="Blues")

tweets_df.hist(bins=30, figsize=(13, 5), color='r')


# - Plot similar figure using seaborn countplot
sns.countplot(tweets_df["label"], label="Count")

# Let's get the length of the messages
tweets_df['length'] = tweets_df['tweet'].apply(len)

tweets_df['length'].plot(bins=100, kind='hist')

tweets_df.describe()

# Let's see the shortest message
tweets_df[tweets_df['length'] == 11]['tweet'].iloc[0]

# Let's see the avarage length message
tweets_df[tweets_df['length'] == 85]['tweet'].iloc[0]

positive = tweets_df[tweets_df['label'] == 0]

positive.head()

negative = tweets_df[tweets_df['label'] == 1]

negative.head()

# Plotting the word-cloud
sentences = tweets_df['tweet'].tolist()
print(len(sentences))

sentences_as_one_string = " ".join(sentences)
print(sentences_as_one_string)

# Plot a WordCloud for all tweets
plt.figure(figsize=(20, 20))
plt.imshow(WordCloud().generate(sentences_as_one_string))

# Plot negative tweets
negative_sentences = negative['tweet'].tolist()
negative_sentences_as_one_string = " ".join(negative_sentences)

plt.figure(figsize=(20, 20))
plt.imshow(WordCloud().generate(negative_sentences_as_one_string))

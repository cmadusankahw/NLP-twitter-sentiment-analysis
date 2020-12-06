import string
import nltk # Natural Language tool kit
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# punctuations in English language
print(string.punctuation)

Test = 'Good morning beautiful people :)... I am having fun learning Machine learning and AI!!'

# PERFORM DATA CLEANING - REMOVE PUNCTUATIONS

# using list notation
Test_punc_removed = [ char for char in Test if char not in string.punctuation ]
print(Test_punc_removed)

# Join the characters again to form the string.
Test_punc_removed_join = "".join(Test_punc_removed)

print(Test_punc_removed_join)


# PERFORM DATA CLEANING - REMOVE STOPWORDS

stopwords.words('english')
Test_punc_removed_join_clean =[ word for word in Test_punc_removed_join.split() if word.lower() not in stopwords.words('english') ]

print(Test_punc_removed_join_clean) # Only important (no so common) words are left


# PERFORM COUNT VECTORIZATION (TOKENIZATION)

sample_data = ['This is the first paper.','This document is the second paper.','And this is the third one.','Is this the first paper?']


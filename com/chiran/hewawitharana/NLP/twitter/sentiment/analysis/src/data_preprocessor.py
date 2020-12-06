import string
import nltk  # Natural Language tool kit

nltk.download('stopwords')
from nltk.corpus import stopwords


# Let's define a pipeline to clean up all the messages
# The pipeline performs the following: (1) remove punctuation, (2) remove stopwords

def message_cleaning(message):
    Test_punc_removed = [char for char in message if char not in string.punctuation]
    Test_punc_removed_join = ''.join(Test_punc_removed)
    Test_punc_removed_join_clean = [word for word in Test_punc_removed_join.split() if
                                    word.lower() not in stopwords.words('english')]
    return Test_punc_removed_join_clean

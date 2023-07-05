import nltk
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class TextPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
    
        self.punctuation = set(string.punctuation)
        
        #Stopwords
        stopwords_en = set(stopwords.words('english'))
        custom_stopwords = [
            'feeling','like','im','know','really',
            'get','feel','want','would','way','one',
            'still','little','bit','ive'     
            ]
        self.stopwords  = list(stopwords_en) + custom_stopwords

        self.lemmatizer = WordNetLemmatizer()

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        preprocessed_text = []
        for text in X:
            tokens = nltk.word_tokenize(text)
            tokens = [self.lemmatizer.lemmatize(token.lower()) for token in tokens]
            tokens = [token for token in tokens if token not in self.stopwords and token not in self.punctuation]
            preprocessed_text.append(' '.join(tokens))
        return preprocessed_text

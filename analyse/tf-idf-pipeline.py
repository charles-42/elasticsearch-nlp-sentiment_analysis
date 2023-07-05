from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
from preprocessing import TextPreprocessor





# Example usage
nlp_pipeline = Pipeline([
    ('preprocessor', TextPreprocessor()),
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Charger le jeu de données à partir du fichier CSV
data = pd.read_csv('data/emotion_final.csv')

X = data['text']
y = data['emotion']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

nlp_pipeline.fit(X_train, y_train)
y_pred = nlp_pipeline.predict(y_test)

# Calculate accuracy for TF-IDF model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy (TF-IDF):", accuracy)

with open('nlp_pipeline.pkl', 'wb') as file:
    pickle.dump(nlp_pipeline, file)

print(type(nlp_pipeline))
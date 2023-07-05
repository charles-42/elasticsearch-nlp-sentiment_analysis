from elasticsearch import Elasticsearch
from faker import Faker
import csv
import random
import pickle
from preprocessing import TextPreprocessor




# Load the pickle file
pickle_path = "/Users/charles/Documents/pythonProject/elasticsearch-nlp-sentiment_analysis/analyse/nlp_pipeline.pkl"
with open(pickle_path, 'rb') as file:
    model = pickle.load(file)

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])

# Nom de l'index Elasticsearch
index_name = 'notes'

def delete_all(es,index_name):
        # Define the query to match all documents
    query = {
        "query": {
            "match_all": {}
        }
    }

    # Delete documents using the delete_by_query API
    response = es.delete_by_query(index=index_name, body=query)

delete_all(es,index_name)


# Instanciation de Faker
fake = Faker()

# Fake patient

patient_list= []
# Generate a tuple of (first_name, last_name)

for i in range(50):
    patient_list.append( (fake.first_name(), fake.last_name()) )

# Chemin vers le fichier CSV
csv_file = 'analyse/data/emotion_final.csv'


# Lecture du fichier CSV et indexation des données
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Génération des valeurs Faker pour les champs nom et prenom
        patient = random.choice(patient_list)
        row['patient_firstname'] = patient[0]
        row['patient_lastname'] = patient[1]
        row['emotion'] = model.predict([row['text']])[0]
        row['confidence'] = model.predict_proba([row['text']]).max()
        row['date'] =  fake.date_between(start_date='-30d', end_date='today').strftime("%Y-%m-%d")
        row['patient_left'] = fake.boolean()
        # Indexation des données dans Elasticsearch
        es.index(index=index_name, document=row)
es.indices.refresh(index=index_name)
es.transport.close()
print("Indexation terminée.")
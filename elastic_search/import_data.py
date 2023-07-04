from elasticsearch import Elasticsearch
from faker import Faker
import csv

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])

# Instanciation de Faker
fake = Faker()

# Fake patient

patient_list= []
# Generate a tuple of (first_name, last_name)

for i in range(50):
    patient_list.append( (fake.first_name(), fake.last_name()) )

# Chemin vers le fichier CSV
csv_file = 'analyse/data/Emotion_final.csv'

# Nom de l'index Elasticsearch
index_name = 'notes'
truc = 1
# Lecture du fichier CSV et indexation des données
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Génération des valeurs Faker pour les champs nom et prenom
        row['nom'] = fake.last_name()
        row['prenom'] = fake.first_name()
        if truc ==1:
            print(row)
            truc +=1

        # # Indexation des données dans Elasticsearch
        # es.index(index=index_name, body=row)

print("Indexation terminée.")
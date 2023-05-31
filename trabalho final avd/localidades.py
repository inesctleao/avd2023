import spacy
import os
import csv

with open('a_mulher_fatal1spl.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

nlp = spacy.load('pt_core_news_sm')
doc = nlp(text)

locations = []

for ent in doc.ents:
    if ent.label_ == "LOC":
        locations.append(ent.text)

from collections import Counter

locations_counts = Counter(locations)

top30_locations = locations_counts.most_common(30)

print(top30_locations)

with open('LOCALIDADESa_mulher_fatal.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Localidade', 'Contagem'])  # Adiciona o cabeçalho das colunas

    for location, count in top30_locations:
        writer.writerow([location, count])

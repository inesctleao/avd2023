import spacy
import os
import csv

with open('amor_de_salvacao1spl.txt', 'r', encoding='UTF-8') as file:
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

with open('LUGARESamor_de_salvacao.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Localidade', 'Contagem']) 
    for location, count in top30_locations:
        writer.writerow([location, count])

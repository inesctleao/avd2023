import spacy
import os
import csv

with open('o_romance_dum_homem_rico1spl.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

nlp = spacy.load('pt_core_news_sm')
doc = nlp(text)

characters = []

for ent in doc.ents:
    if ent.label_ == "PER":
        characters.append(ent.text)

from collections import Counter

characters_counts = Counter(characters)

top30_characters = characters_counts.most_common(30)

print(top30_characters)

with open('Entidades_oromancedumhomemrico.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Personagem', 'Contagem']) 

    for character, count in top30_characters:
        writer.writerow([character, count])

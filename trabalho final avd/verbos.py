import spacy
import os
import csv
from collections import Counter

with open('onde_esta_a_felicidade1spl.txt', 'r', encoding='UTF-8') as file:
    text = file.read()

nlp = spacy.load('pt_core_news_sm')
doc = nlp(text)

dicionario = dict()

for token in doc:
    if token.pos_ == "VERB":
        if token.lemma_ in dicionario.keys():
            dicionario[token.lemma_] += 1
        else:
            dicionario[token.lemma_] = 1

verb_counts = Counter(dicionario)
top20_verbs = verb_counts.most_common(20)

print(top20_verbs)

with open('VERBOSondeestaafelicidade.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Verbo', 'Contagem']) 

    for verb, count in top20_verbs:
        writer.writerow([verb, count])


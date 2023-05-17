import spacy
import sys
import csv

path = sys.argv[1]

f = open(path, "r", encoding="utf8")

text = f.read()

nlp = spacy.load("pt_core_news_sm")
doc = nlp(text)
dicionario = dict()

for entity in doc.ents:
    if entity.label_ == 'PER' or entity.label_ == 'LOC':
        if entity.text in dicionario.keys():
            dicionario[entity.text] += 1
        else:
            dicionario[entity.text] = 1
print(dicionario)

with open('ondeestaafelicidade.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["localidades" , "contagem"])
    for key,value in dicionario.items():
        writer.writerow([key , value])
        
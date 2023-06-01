import spacy
import csv
from collections import Counter

nlp = spacy.load('pt_core_news_sm')

with open('o_romance_dum_homem_rico1spl.txt', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

adjectives = Counter()

for token in doc:
    if token.pos_ == 'ADJ':  
        adjectives[token.lemma_] += 1  

top20_adjectives = adjectives.most_common(20)

with open('adjetivos_oromancedumhomemrico.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Adjetivo', 'Frequência'])
    writer.writerows(top20_adjectives)

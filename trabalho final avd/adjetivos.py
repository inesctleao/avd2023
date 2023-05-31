import spacy
import csv
from collections import Counter

# Carregar modelo linguístico em português
nlp = spacy.load('pt_core_news_sm')

# Abrir o arquivo do livro
with open('MariaMoises.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# Processar o texto com o modelo do Spacy
doc = nlp(texto)

# Extrair adjetivos do texto e contar a frequência
adjetivos = [token.text for token in doc if token.pos_ == 'ADJ']
frequencia_adjetivos = Counter(adjetivos)

# Imprimir a frequência de cada adjetivo
for adjetivo, frequencia in frequencia_adjetivos.items():
    print(f'{adjetivo}: {frequencia}')
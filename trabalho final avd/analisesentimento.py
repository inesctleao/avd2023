import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

caminho_arquivo = "onde_esta_a_felicidade1spl.txt"

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

capitulos = texto.split('# Capítulo')

for i, capitulo in enumerate(capitulos[1:]):
    sentiment = sia.polarity_scores(capitulo)
    print(f"Sentimento do Capítulo {i+1}: {sentiment}")

import csv
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))

def extrair_palavras_chave(texto):
    texto = texto.translate(str.maketrans('', '', string.punctuation)).lower()
    palavras = texto.split()
    palavras = [palavra for palavra in palavras if palavra not in stop_words]
    contagem_palavras = Counter(palavras)
    return contagem_palavras

with open('onde_esta_a_felicidade1spl.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

palavras_chave = extrair_palavras_chave(texto)

top_palavras_chave = palavras_chave.most_common(10)

nome_arquivo_csv = 'felicidadepalavras_chave.csv'

with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['Palavra-chave', 'Frequência'])  # Cabeçalho das colunas
    
    for palavra, frequencia in top_palavras_chave:
        writer.writerow([palavra, frequencia])

print("As 10 principais palavras-chave foram extraídas e salvas com sucesso no arquivo", nome_arquivo_csv)



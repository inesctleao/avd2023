import csv
import re
from collections import Counter

def extrair_adverbios(texto):
    padrao = r'\b\w+mente\b'
    adverbios = re.findall(padrao, texto, re.IGNORECASE)
    return adverbios

def contar_frequencia(adverbios):
    contagem = Counter(adverbios)
    return contagem

def criar_csv(resultado, arquivo):
    with open(arquivo, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Adverbio', 'Frequencia'])
        writer.writerows(resultado)
    print(f'O arquivo {arquivo} foi criado com sucesso!')

with open('onde_esta_a_felicidade1spl.txt', 'r') as arquivo_txt:
    texto = arquivo_txt.read()

adverbios = extrair_adverbios(texto)

frequencia = contar_frequencia(adverbios)

top_20 = frequencia.most_common(20)

criar_csv(top_20, 'resultado.csv')

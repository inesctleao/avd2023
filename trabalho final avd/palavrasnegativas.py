import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('vader_lexicon')

def extract_negative_words(text):
    sid = SentimentIntensityAnalyzer()
    tokens = word_tokenize(text)
    negative_words = [token.lower() for token in tokens if sid.polarity_scores(token)['compound'] < 0]

    return negative_words

def save_negative_words_to_csv(negative_words, output_file):
    word_counts = Counter(negative_words)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(word_counts.most_common())

# Caminho para o arquivo de texto
input_file = 'o_romance_dum_homem_rico1spl.txt'

# Caminho para o arquivo CSV de saída
output_file = 'FINALNEGo_romance_dum_homem_rico1spl.csv'

# Leitura do arquivo de texto
with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

# Extração das palavras negativas
negative_words = extract_negative_words(text)

# Salvando as palavras negativas e suas frequências em um arquivo CSV
save_negative_words_to_csv(negative_words, output_file)

import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def extract_lemmas(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))  # Altere para o idioma desejado

    tokens = nltk.word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalnum() and token.lower() not in stop_words]

    return lemmas

def save_lemmas_to_csv(lemmas, output_file):
    fdist = FreqDist(lemmas)
    top_lemmas = fdist.most_common(50)  # Seleciona os 50 lemas mais frequentes
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Lemma', 'Frequency'])
        for lemma, freq in top_lemmas:
            writer.writerow([lemma, freq])

# Caminho para o arquivo de texto
input_file = 'onde_esta_a_felicidade1spl.txt'

# Caminho para o arquivo CSV de saída
output_file = 'TOP50onde_esta_a_felicidade.csv'

# Leitura do arquivo de texto
with open(input_file, 'r') as file:
    text = file.read()

# Extração dos lemas
lemmas = extract_lemmas(text)

# Salvando os 50 lemas mais frequentes em um arquivo CSV
save_lemmas_to_csv(lemmas, output_file)

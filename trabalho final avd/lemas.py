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
    stop_words = set(stopwords.words('english'))

    tokens = nltk.word_tokenize(text)
    lemmas = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalnum() and token.lower() not in stop_words]

    return lemmas

def save_lemmas_to_csv(lemmas, output_file):
    fdist = FreqDist(lemmas)
    top_lemmas = fdist.most_common(50) 
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Lemma', 'Frequency'])
        for lemma, freq in top_lemmas:
            writer.writerow([lemma, freq])

input_file = 'o_romance_dum_homem_rico1spl.txt'

output_file = 'TOP50oromancedumhomemrico.csv'

with open(input_file, 'r') as file:
    text = file.read()

lemmas = extract_lemmas(text)

save_lemmas_to_csv(lemmas, output_file)

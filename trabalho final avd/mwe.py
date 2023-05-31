import nltk
import csv

# Baixe os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_mwes_from_text(text):
    mwes = []
    sentences = nltk.sent_tokenize(text)  # Divide o texto em frases
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)  # Divide cada frase em palavras
        pos_tags = nltk.pos_tag(words)  # Realiza marcação de partes do discurso (POS tagging)
        grammar = r"""
            MWE: {<NN.*><IN><NN.*>}  # Padrão para extrair MWEs com substantivos seguidos de preposição e substantivos
                 {<JJ.*><NN.*>}      # Padrão para extrair MWEs com adjetivos seguidos de substantivos
        """
        cp = nltk.RegexpParser(grammar)
        tree = cp.parse(pos_tags)  # Realiza análise de chunking para encontrar MWEs
        for subtree in tree.subtrees():
            if subtree.label() == 'MWE':
                mwe = ' '.join([token[0] for token in subtree.leaves()])  # Une as palavras da MWE
                mwes.append(mwe)
    return mwes

# Caminho do arquivo de texto de entrada
input_file_path = 'a_mulher_fatal1spl.txt'

# Caminho do arquivo CSV de saída
output_file_path = 'a_mulher_fatal.csv'

# Lê o conteúdo do arquivo de texto
with open(input_file_path, 'r') as file:
    text = file.read()

# Extrai as MWEs do texto
mwes = extract_mwes_from_text(text)

# Escreve as MWEs em um arquivo CSV
with open(output_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['MWE'])
    writer.writerows([[mwe] for mwe in mwes])

print("As MWEs foram extraídas e salvas no arquivo CSV com sucesso!")

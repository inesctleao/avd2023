import spacy
from spacy.tokens import Span

# Função para calcular a pontuação de sentimento de uma sentença
def calcular_pontuacao(sentenca):
    # Lógica para calcular a pontuação de sentimento da sentença
    # Substitua esta função pela lógica de análise de sentimento que você deseja utilizar
    return 0.5

# Registrando a extensão "sentiment" no objeto Span
Span.set_extension('sentiment', getter=calcular_pontuacao)

# Carregue o modelo de linguagem do spaCy
nlp = spacy.load('en_core_web_sm')

# Caminho para o arquivo do documento
caminho_documento = "./amor_de_salvacao1spl.txt"

# Leitura do arquivo
with open(caminho_documento, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# Processamento do texto com spaCy
doc = nlp(texto)

# Divisão do texto em capítulos
capitulos = texto.split("Capítulo")

# Realize a análise de sentimento para cada capítulo
for i, capitulo in enumerate(capitulos[1:], start=1):  # Ignorar o primeiro elemento vazio
    capitulo_doc = nlp(capitulo)
    
    # Realize a análise de sentimento para cada sentença do capítulo
    pontuacoes = []
    for sentenca in capitulo_doc.sents:
        pontuacao = sentenca._.sentiment
        pontuacoes.append(pontuacao)
    
    # Calcule a pontuação geral do capítulo
    pontuacao_geral = sum(pontuacoes) / len(pontuacoes)
    
    # Imprima a pontuação geral do capítulo
    print("Pontuação do Capítulo", i, ":", pontuacao_geral)

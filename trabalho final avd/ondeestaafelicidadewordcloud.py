import matplotlib.pyplot as plt
from wordcloud import WordCloud

texto = "dizer ter querer fazer poder saber dar haver vir ver ser dever falar ir entrar parecer deixar conhecer sair passar."

wordcloud = WordCloud().generate(texto)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

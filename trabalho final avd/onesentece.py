filename = "Camilo-A_mulher_fatal.txt"

infile = open(filename, 'r')
data = infile.read()
infile.close()


frases = data.split(". ")  # Divide o texto em uma lista de frases usando o ponto seguido de um espaço como separador
f = open("a_mulher_fatal1spl.txt", "a")
for frase in frases:
    f.write(frase+"\n")      	
      # Imprime cada frase em uma linha separada

f.close()

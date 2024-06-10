import os
# open("arquivo","modo")
# - r - leitura
# - a - adição append / incrementar
# - w - escrita 
# - x - criar arquivo
# - r+ - leitura + escrita


#arquivo = open("Aula12/text3.txt","r")

#print(arquivo.readable()) # readable() nos retorna se o arquivo pode ser lido ou não 
#print(arquivo.read()) # retorna as palavras escritas no txt
#print(arquivo.readline()) # readline() retorna só a primeira linha do arquivo.
#print(arquivo.readlines()) # retorna uma lista onde cada linha é um item.
#arquivo.write("\nSQL") # o write() aliado ao modo "a", só adiciona uma nova palavra
#lista = arquivo.readlines()
#print(lista[3])

#arquivo.close()# precisamos fechar o arquivo sempre ao final da#s operações.
if os.path.exists("Aula12/text3.txt"):
    os.remove("Aula12/text3.txt")
else:
    print("não posso apagar o que não existe")

print("hellow moto :/ :)")
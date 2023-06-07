"""
split e join com list e str
split - divide uma string  #se nao passar um argumento, 
vai dividir nos espaços em branco
join - une uma string
"""
frase = 'Olha so que, coisa interessante'
lista_frases_crua = frase.split(', ') #virgula + espaço


lista_frases = []
for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())  #strip corta os espaços do começo e do fim
# rstrip (corta da direita)  //  lstrip (corta da esquerda)
# print(lista_frases_crua)
# print(lista_frases)

frases_unidas = '*'.join('brunazamboni') # '' separador
print(frases_unidas)

frases_unidas_lista = ', '.join(lista_frases) # '' separador
print(frases_unidas_lista)
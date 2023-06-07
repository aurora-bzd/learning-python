"""
enumerate - enumera iteraveis (indices)
"""

lista = ['Bruna', 'Maria', 'Gezuino']

#lista_enumerada = enumerate(lista)
# ao colocar o enumerate numa variavel, ele consome apos o for

for indice, nome in enumerate(lista):
    print(indice, nome)
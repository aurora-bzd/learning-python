"""
Introduçao ao desempacotamento 
"""

nomes = ['Bruna', 'Elena', 'Jhons']
nome1, nome2, nome3 = nomes 
# que eh a mesma coisa que: 
#nome1, nome2, nome3 = ['Bruna', 'Elena', 'Jhons']
print(nome1)

palavra, *resto = ['Casa', 'Carro', 'Gaveta', 'Gato']
print(resto)
#*resto -> restante da lista fica empacotado em uma variavel chamada "resto"
# se usar *_ -> vai dizer para outro dev que a lista ta ali, mas ela nao vai ser utilizada

_, _, _, palavra, *_ =['Casa', 'Carro', 'Gaveta', 'Gato']
print(palavra)
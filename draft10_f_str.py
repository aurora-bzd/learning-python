# Introduçao a f-strings (formataçao de strings)

nome = "Bruna"
altura = 1.53
peso = 50
imc = peso / altura ** 2

linha1 = f'{nome} tem {altura:.2f} de altura'
linha2 = f'pesa {peso} quilos e seu imc eh'
linha3 = f'{imc}'

print(linha1, linha2, linha3, sep="\n")

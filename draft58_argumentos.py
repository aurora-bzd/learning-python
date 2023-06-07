"""
Argumentos nomeados e nao nomeados em funcoes Python
Argumentos nomeados tem nome com sinal de igual
Argumentos nao nomeados recebe apenas o argumento (Valor)
"""

def soma (x,y):
    #Definicao
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)

soma(1, 2)
soma(y = 2, x = 1)
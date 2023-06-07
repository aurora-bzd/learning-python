"""
Introduçao as funçoes (def) em Python
Funcoes sao trechos de codigo usados para replicar determinada açao ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos) e retornar um vaor especifico.
Por padrao, funcoes Python retornam None (nada)
"""

def imprimir(a,b,c):
    print(a,b,c)
imprimir(1,2,3)

def saudacao (nome = 'Sem nome'):
    print(f'Ola, {nome}!')
saudacao('Bruna')
saudacao('Ana')
saudacao('Luiz')
saudacao()


"""
Escopo de Funcoes em Python
Escopo significa o local onde aquele codigo pode atingir
Existe o escopo global e local
O escopo global eh o escopo onde todo o codigo eh alcançavel
O escopo local eh o escopo onde apenas nomes do mesmo local podem ser alcançados
Nao temos acesso a nomes de escopos internos nos escopos externos
A palavra "global" faz uma variavel do escopo externo ser a mesma no escopo interno
global x -> vai indicar que esta utilizando a variavel global
"""

x = 1

def escopo():
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print (x, y)

    outra_funcao()
    print(x)
    
print(x)
escopo()
print(x)

print('------------------------------')

x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print (x, y)

    outra_funcao()
    print(x)
    
print(x)
escopo()
print(x)

print('------------------------------')


x = 1

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print (x, y)

    outra_funcao()
    print(x)
    
print(x)
escopo()
print(x)

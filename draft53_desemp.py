"""
Desempacotamento em chamadas
de metodos e funções
"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'eh', 'legal'

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)

salas = [
    #0         #1
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine', ], #1
    #0       #1       #2        #3
    ['Luiz', 'Joao', 'Eduarda', (0, 1, 2, 3, 4)], #2
] 

print(*salas, sep='\n')
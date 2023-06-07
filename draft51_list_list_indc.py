"""
Lista de listas e seus indices
"""

salas = [
    #0         #1
    ['Maria', 'Helena', ], #0
    #0
    ['Elaine', ], #1
    #0       #1       #2        #3
    ['Luiz', 'Joao', 'Eduarda', (0, 1, 2, 3, 4)], #2
]                               #0  #1 #2 #3 #4

print (salas[0][1])
 #para acessar o valor de uma lista dentro de uma lista:
 #o primeiro [] vai indicar a posiçao na lista central
 #e o segundo [] vai indicar a posicao na lista indicada

print(salas [2][3][2])

for sala in salas:
    print(f'A sala eh {sala}')
    for aluno in sala:
        print(aluno)
"""
Cuidados com dados mutaveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na memoria (mutavel)
"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a # as duas listas vao apontar para um mesmo lugar na memoria
lista_c = lista_a.copy() # vai copiar os itens da lista a numa nova lista c, 
#porem o que for modificado posteriormente na lista a, nao vai ser inserido na lista c

lista_a[0] = 'Qualquer coisa'
print('Lista A =', lista_a)
print('Lista B =', lista_b)
print('Lista C =', lista_c)


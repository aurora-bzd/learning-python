"""
Listas em Python
Tipo de list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: 
    append - adiciona um item ao final da lista
    insert - adiciona um item no indice escolhido
    pop - remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [123, True, 'Bruna', 1.2, []]
print(lista)
print(lista[4], type(lista[4]))

lista[2] = 'Bruna Zamboni'
print(lista[2])
print (lista)

#-------------------------------------------
print('                                      ','<3<3<3<3<3<3<3<3<3<3<3<3<3<3', '                                      ')
#-------------------------------------------

lista_2 = [10, 20, 30, 40, 50]
del lista_2[4] #o ideal eh adicionar ou retirar itens do final da lista [-1]
print(lista_2)

lista_2.append(50) # adiciona um item ao final da lista
print(lista_2)

ultimo_valor = lista_2.pop() #pop vazio = remove o ultimo item da lista
print(lista_2, 'Removido', ultimo_valor)

remover_id_2 = lista_2.pop(2) # pode remover um indice especifico usando o pop
print(lista_2, 'Removido', remover_id_2)

lista_3 = [1, 2, 3, 4, 5]
print('Lista 3 =', lista_3)
lista_3.clear() #limpou a lista
print('Lista 3 =', lista_3)

print('Lista 2 ', lista_2)
lista_2.insert(0, 22) # inseri um numero na lista, o 1. arg eh o indice, e o 2. arg eh o item inserido
print('Lista 2 ', lista_2)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print('listaA + listaB = listaC',lista_c)

lista_a.extend(lista_b) # insere a lista b na lista a
print('Extend a(b)', lista_a)




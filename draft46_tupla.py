""" 
Tipo tupla - Uma lista imutavel
- nao colocando os colchetes 
- utilizar parenteses se quiser
- converter lista pra tupla -> lista = tuple(lista)
- converter tupla pra lista -> tupla = list(tupla)
"""

nomes = 'Bruna', 'Elena', 'Jhons'
print(nomes)

nomes = ('Pedro', 'Paulo', 'Paloma')
print(nomes)

nomes_lista = ['Pedro', 'Paulo', 'Paloma']
ex_lista = tuple(nomes_lista)
print(ex_lista)

tupla_lista = 'Pedro', 'Paulo', 'Paloma'
ex_tupla = list(tupla_lista)
print(ex_tupla)

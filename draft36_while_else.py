"""(
while/else
"""

string = 'valor qualquer'

i = 0
while i < len(string):
    letra = string[i]
    i += 1

    break ##

    print(letra)
    i += 1

else:
    print('O else foi executado')

print('Fora do while')

#quando tem um brak - nada mais eh executado, inclusive o else
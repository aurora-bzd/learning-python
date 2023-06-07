"""
Interpolaçao basica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço eh R$%f' %(nome,preco)
print(variavel)

variavel = '%s, o preço eh R$%.2f' %(nome,preco)
print(variavel)

print('O hexadecimal de %d eh %x' % (15,15))
print('O hexadecimal de %d eh %04x' % (15,15))

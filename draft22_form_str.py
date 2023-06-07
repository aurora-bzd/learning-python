"""
Formataçao basica de strings
s - string
d - inteiro
f - float
.<numero de digitos>f
x ou X - Hexadecial
(Caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o numero a aparecer antes do zero
Sinal - + ou -
Ex.: 0>-100,1f
Conversion flags - !r !s !a
"""

variavel = 'AB'
print(f'{variavel}.')
print(f'{variavel:0>10}.')
print(f'{variavel:0<10}.')
print(f'{variavel:0^10}.')

print(f'{1000.45648546456:0=+10,.1f}')

print(f'O hexadecimal de 1500 eh {1500:08X}')

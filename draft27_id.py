"""
Flag(Bandeira) - Marcar um local
None = Nao valor
is e is not = eh ou nao eh (tipo, valor, identidade)
id = Identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')

if passou_no_if is None:
    print('Nao passou no IF')
else:
    print('Passou no IF')
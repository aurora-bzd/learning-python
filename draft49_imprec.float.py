"""
Imprecisao de ponto flutuante
Double-precision floating-point format IEEE 754
"""
import decimal #vai resolver o problema usando str

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') # vira string, mas acerta o numero final

print(round(numero_3,2)) # acertar o numero, continua float, arredonda


numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_1 + numero_2

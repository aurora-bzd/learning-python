"""
Iteravel = str, range, etc ( __iter__)
Iterador = quem sabe entregar um valor por vez
next = me entrega o proximo valor
iter = me entregar seu iterador
"""

texto = "Luiz"  # iteravel
iteratador = iter(texto)  # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

# eh isso que acontece em: #for letra in texto
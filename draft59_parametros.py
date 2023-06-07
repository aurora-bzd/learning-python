"""
Valores padrao para parametros
Ao definir uma funcao, os parametros podem ter valores padrao.
Caso o valor nao seja enviado para o parametro, o valor padrao sera usado.
Refatorar: editar o seu codigo.
0 eh considerado um valor falsy
valor padrao neste caso = None
Todo parametro que vier depois do parametro que recebeu um valor padrao,
precisa receber um valor padrao tbm.
"""

def soma(x, y, z  = None):
    if z is not None:
        print(f'{x=}{y=}{z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1,20)
soma(3,5)
soma(7,9,0)
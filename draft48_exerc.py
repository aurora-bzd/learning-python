lista = []

import os

while True:
    print('Selecione uma opçao')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Nao foi possivel apagar este indice')


    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
        



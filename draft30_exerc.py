nome = input('Informe o seu primeiro nome: ')
nome_len = len(nome)

if nome_len > 1:

    if nome_len <= 4:
        print('Seu nome eh curto')

    elif nome_len >= 5 and nome_len <= 6:
        print('Seu nome eh do tamanho normal')

    else:
        print('Seu nome eh muito grande')

else:
    print('Digite mais de uma letra.')



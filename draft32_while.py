"""
Repetiçoes
while(enquanto)
Executa uma açao enquanto uma condiçao for verdadeira
Looping infinito: quando um codigo nao tem fim
break = quebra o laço, tudo que vier dps nao sera executado
continue = pula o looping -> tudo ate o continue segue normal e dps ele volta pro inicio do laço
"""

# condicao = True

# while condicao:
#     nome = input('qual eh o seu nome? ')
#     print(f'Seu nome eh {nome}')

#     if nome == 'sair':
#         break

#     print('Acabou')

#-----------------------------------------


# contador = 0

# while contador <= 10:
#     print(contador)
#     contador = contador + 1

# print("OVER")

#--------------------------------------------

 
# contador = 0

# while contador <= 100:
#     contador += 1

#     if contador == 6:
#         print('Nao vou mostrar o 6')
#         continue

#     if contador >=10 and contador <=27:
#         continue

#     print(contador)

#     if contador == 40:
#         break

# print("OVER")


#-----------------------------


qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')


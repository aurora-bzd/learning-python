# Operadores Logicos
# and (e) or (ou) nor (nao
# and - todas as condicoes precisam ser verdades
# se qualquer valor for considerado falso, a expressao inteira sera avaliada naquele valor
# sao consideradas falsy 00.0 '' False
# tambem existe o tipo None que eh usado para representar um nao valor

entrada = input('[E]ntrar [Sair].')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E'and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliaçao de curto circuito -> checa ate aonde precisa e nao checa mais
print(True and False and True)
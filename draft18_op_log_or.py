# or - Qualquer condicao verdadeira avalia toda a expressao como verdadeira.
# Se qualquer valor for considerado verdadeiro, a expressao inteira sera avaliada naquele valor.

entrada = input('[E]ntrar [Sair].')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliacao de curto circuito

print(0 or False or True)
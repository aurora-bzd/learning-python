#funçao format = o método format() em python serve basicamente para criar uma string que contém 
#campos entre chaves que são substituidos pelos argumentos de format.

a = 'A'
b = 'B'
c = 1.1
formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)

print(formato)
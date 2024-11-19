# Escreva as seguintes expressões algébricas em linguagem Python:

# a) O somatório dos 5 primeiros números inteiros e positivos
print(1 + 2 + 3 + 4 + 5)

# b) A média entre 23, 19 e 31
media = (23 + 19 + 31) / 3
print(media)

# c) O número de vezes que 73 cabem em 403
cabe = 403 // 73
print(f'O número 73 cabe {cabe} vezes em 403')

# d) A sobra quanto 403 é dividido por 73
sobra = 403 % 73
print(f'A sobra é {sobra}')

# Escreva as seguintes expressões algébricas em linguagem Python:

# e) 2 elevado à 10 potencia
print(2 ** 10)

# f) O valor absoluto da diferença entre 54 e 57
print(abs(54 - 57))

# g) O menor valor entre 34, 29, 31
print(min(34, 29, 31))

# Escreva as expressões em Python para:

# a) Atribuir o valor inteiro 3 à variável a
# b) Atribuir o valor 4 à variável b
# c) Atrinuir à variável c o valor da expressão a * a + b * b

a = 3
b = 4
c = a * a + b * b

print(c)

# Execute as seguintes atribuições
# s1 = 'ant'
# s2 = 'bat'
# s3 = 'cod'

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Agora utilizando operadores + e *, crie as saídas a seguir:
# a) 'ant bat cod'
# b) 'ant ant ant ant ant ant ant ant ant ant'
# c) 'ant bat bat cod cod cod'
# d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
# e) 'batbatcod batbatcod batbatcod batbatcod batbatcod'

print(s1, s2, s3)
print(10 * (s1 + ' '))
print(s1, 2 * (' ' + s2), 3 * (' ' + s3))
print(7 * (s1 + ' ' + s2 + ' ' ))
print(5 * ((2 * s2 + s3) + ' '))
# Escreva as sdeguintes expressões booleanas
# em linguagem Python
#  a) O somatório de 2 com 2 é menor que 4
print(2 + 2 < 4)

#  b) O valor 7 // 3 é igual 1 + 1
print(7 // 3 == 1 + 1)

#  c) A soma de 3 elevado ao quadrado com 4 
# elevado ao quadrado é igual a 25
print(3**2 + 4**2 == 25)

#  d) A soma de 2, 4 e 6 é maior que 12
print( 2 + 4 + 6 > 12)

print('')


# Escreva as sdeguintes expressões booleanas
# em linguagem Python
#  a) 1387 é divisível por 19
print(1387 % 19 == 0)

#  b) 31 é par
print(31 % 2 == 0)

#  c) O menor valor entre: 34, 29 e 31 é menor que 30
print(min(34, 29, 31) < 30)

print('')


# Traduza as afirmações a seguir para condicionais em Python
#  a) Se idade é maior que 60, escreva: Você tem direitos aos benefícios
idade = 61
if(idade > 60):
    print('Você tem direito aos benefícios')
else: 
    print('Você não tem direito aos benefícios')

#  b) Se dano é maior que 10 e escudo é igual a 0, escreva: Você está morto!
dano = 13
escudo = 0
if(dano > 10 and escudo == 0):
    print('Você está morto!')
else:
    print('Você sobreviveu!')
    
#  c) Se pelo menos uma das variáveis booleanas
# norte, sul, leste e oeste resultarem em True, 
# escreva: Você escapou!
norte = False
sul = True
leste = False
oeste = False

if(norte or sul or leste or oeste):
    print('Você escapou!')
else:
    print('Rapaz, ficasse preso!')

print('')


# Traduza as afirmações a seguir para condicionais em Python
#  a) Se ano é divisível por 4, escreva: Pode ser um ano bissexto.
# Caso contrário, escreva: Definitivamente não é um ano bissexto
ano = 2024
if(ano % 4 == 0): 
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto') 

#  b) Se ambas as variáveis booleanas cima e baixo forem True, escreva:
# Decida-se, caso contrário, escreva: Você escolheu um caminho
cima = True
baixo = True

if(cima or baixo):
    print('Decida-se')
else:
    print('Você escolheu um caminho!')
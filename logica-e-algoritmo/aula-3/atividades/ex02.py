# Faça um algoritmo que receba três
# valores, representando os lados de um triângulo fornecidos pelo usuário.
# Verifique se os valores formam um triângulo e classifique como:
# a) Equilátero (três lados iguais);
# b) Isósceles (dois lados iguais);
# c) Escaleno (três lados diferentes).
# Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser
# igual a zero e um lado não pode ser maior do que a soma dos outros dois.

a = int(input('Digite o 1º lado do triângulo: '))
b = int(input('Digite o 2º lado do triângulo: '))
c = int(input('Digite o 3º lado do triângulo: '))

if(a > 0 and b > 0 and c > 0):
    if(a + b > c and b + c > a and c + a > b):
        if(a == b and b == c and c == a):
            print('Triângulo equilátero')
        elif(a == b or b == c or c == a):
            print('Triângulo isósceles')
        else: 
            if(a != b and b != c and c != a):
                print('Triângulo escaleno')
    else: 
        print('Um dos valores precisa se encaixar na seguinte regra do triângulo: ')
        print('-- Um lado não pode ser maior do que a soma dos outros dois')
else: 
    print('Um dos valores precisa se encaixar na seguinte regra do triângulo: ')
    print('-- Nenhum dos lados pode ser igual a zero')
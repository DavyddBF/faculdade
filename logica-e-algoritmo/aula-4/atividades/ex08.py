# Escreva um algoritmo que encontre todos os números primos de 2 até 99.
# Imprima na tela todos eles.

print('Números primos de 2 até 99:')
for numero in range(2, 100, 1):
    flag = 0
    for i in range(2, numero, 1):
        if(numero % i == 0):
            flag = 1
            break
    if(flag == 0):
        print(numero)
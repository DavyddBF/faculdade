# Escreva um algoritmo que leia dois
# valores e imprima na tela o resultado da multiplicação de ambos. Porém, para
# calcular a multiplicação, utilize somente operações de soma e subtração.
# Lembrando que uma multiplicação pode ser considerada como um
# somatório sucessivo. Utilize esta lógica para construir seu algoritmo

x = int(input('Digite um valor a ser multiplicado: '))
y = int(input('Digite outro valor a ser multiplicado: '))

cont = 1
multi = 0

while(cont <= x):
    multi += y
    cont += 1
print(f'O resultado da multiplicação: {x} x {y} = {multi}')
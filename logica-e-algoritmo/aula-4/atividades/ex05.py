# Vamos revisitar o exercício da tabuada que você desenvolveu na seção
# 2.1, mas um pouco modificado.
# Escreva um algoritmo que calcule e exiba a tabuada de um número
# escolhido e digitado pelo usuário. A tabuada deve ser calculada até um
# determinado número n, também fornecido pelo usuário. Implemente o laço
# usando for. 

num = int(input('Digite um número a ser calculado a sua tabuada: '))

print(f'Tabuada do número {num}')

for i in range(1, 10 + 1, 1):
    print(f'{num} x {i} = {num * i}')
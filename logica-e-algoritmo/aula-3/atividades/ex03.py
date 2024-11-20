# Escreva um algoritmo que leia dois valores
# numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição
# (+), subtração (-), multiplicação (*) ou divisão (/). Exiba na tela o resultado da
# operação desejada.

print('Qual operação matemática você deseja usar?')
print(' 1 - Adição')
print(' 2 - Subtração')
print(' 3 - Multiplicação')
print(' 4 - Divisão')

operacao = int(input(': '))
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if(operacao == 1):
    total = n1 + n2
    print(f'{n1} + {n2} = {total}')
elif(operacao == 2):
    total = n1 - n2
    print(f'{n1} - {n2} = {total}')
elif(operacao == 3):
    total = n1 * n2
    print(f'{n1} * {n2} = {total}')
elif(operacao == 4):
    total = n1 / n2
    print(f'{n1} / {n2} = {total}')
else: print('Operação inválida')
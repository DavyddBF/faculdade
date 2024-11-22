# Escreva um algoritmo que
# obtenha do usuário um valor inicial e um valor final. Para este intervalo
# especificado pelo usuário, calcule e mostre na tela:
# a. A quantidade de números inteiros e positivos;
# b. A quantidade de números pares;
# c. A quantidade de números impares;
# d. A respectiva média de cada um dos itens anteriores;
# Será necessário criar uma variável distinta para cada somatório, para
# cada quantidade e para cada média solicitada.

inicial = int(input('Digite um valor inicial: '))
final = int(input('Digite um valor final: '))
qtdPositivo = 0
qtdPar = 0
qtdImpar = 0
somaPositivo = 0
somaPar = 0
somaImpar = 0

i = inicial
if(inicial < final):
    while(i <= final):
        if(i > 0):
            qtdPositivo += 1
            somaPositivo += i
        if(i % 2 == 0):
            qtdPar += 1
            somaPar += i
        else:
            qtdImpar += 1
            somaImpar += i
        i += 1

    mediaPositivo = somaPositivo / qtdPositivo
    mediaPar = somaPar / qtdPar
    mediaImpar = somaImpar / qtdImpar

    print(f'Quantidade de valores positivos: {qtdPositivo}')
    print(f'Média de valores positivos: {mediaPositivo}')
    print(f'Quantidade de números pares: {qtdPar}')
    print(f'Média de números pares: {mediaPar}')
    print(f'Quantidade de números impares: {qtdImpar}')
    print(f'Média de números impares: {mediaImpar}')
else: 
    print('Você digitou um valor inicial maior ou igual ao final')
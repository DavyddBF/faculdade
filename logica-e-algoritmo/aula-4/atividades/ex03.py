# Escreva um algoritmo que leia números inteiros via teclado. Somente
# valores positivos devem ser aceitos pelo programa.
# Ao final da execução, informe a média dos valores digitados. Realize a
# implementação com as instruções break e continue, e trabalhe com operações
# lógicas Truthy e Falsey. Não esqueça de empregar também operadores
# especiais de atribuição.

soma = 0
qtdNum = 0
x = 0

while True: 
    x = int(input('Digite um valor inteiro: '))
    if(x < 0):
        continue
    if(not x):
        break
    soma += x
    qtdNum += 1

media = soma / qtdNum

print('')
print(f'Valor somado: {soma}')
print(f'Quantidade de números digitados: {qtdNum}')
print('')
print(f'A média dos valores digitados é: {media}')
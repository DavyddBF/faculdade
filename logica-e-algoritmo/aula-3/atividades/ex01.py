# Escreva um algoritmo em Python em que o usuário escolhe se ele quer
# comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu
# com a opção 1 para maçã, 2 para laranja e 3 para banana.
# Após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
# O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo
# na tela.
# Considere que uma maçã custa R$ 2,30, uma laranja R$ 3,60 e uma
# banana 1,85.

print('Escolha qual fruta comprar: ')
print(' 1 - Maçãs')
print(' 2 - Laranja')
print(' 3 - Banana')

escolha = int(input(': '))
unidades = int(input('Quantas da fruta escolhida você deseja? '))

if(escolha ==  1):
    preco = unidades * 2.30
    print(f'Você comprou {unidades} maçã(s). O valor total ficou R${preco}')
elif(escolha == 2) :
    preco = unidades * 3.60
    print(f'Você comprou {unidades} laranja(s). O valor total ficou R${preco}')
elif(escolha == 3) :
    preco = unidades * 1.85
    print(f'Você comprou {unidades} banana(s). O valor total ficou R${preco}')
else: print('Produto não encontrado! Execute novamente o programa!')
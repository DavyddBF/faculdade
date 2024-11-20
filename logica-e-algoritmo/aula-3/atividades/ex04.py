# Uma loja de departamentos está oferecendo diferentes formas de
# pagamento, conforme opções listadas a seguir. Faça um algoritmo que leia o
# valor total de uma compra e calcule o valor do pagamento final de acordo com a
# opção escolhida.
# Se a escolha for por pagamento parcelado, calcule também o valor de
# cada parcela. Ao final, apresente o valor total da compra e o valor das parcelas:
# • Pagamento à vista – conceder desconto de 5%;
# • Pagamento em 3x – o valor não sofre alterações;
# • Pagamento em 5x – acréscimo de 2%;
# • Pagamento em 10x – acréscimo 8%.

print(5 * '-' + ' Lojas PagueBem ' + 5 * '-')
valor = float(input('Digite o valor do produto escolhido: '))

print(5 * '-' + ' Pagamento ' + 5 * '-')
print('')
print('Selecione a forma de pagamento')
print(' 1 - À vista')
print(' 2 - Parcelas de 3x')
print(' 3 - Parcelas de 5x')
print(' 4 - Parcelas de 10x')

op = int(input(': '))

if(op == 1):
    total = valor - (valor * (5 / 100))
    print(f'Certo!! O seu disconto à vista é 5%. O valor final do seu produto fica R${total:.2f}')
elif(op == 2):
    parcela = valor / 3
    print(f'Certo!! 3 vezes de {parcela}. O valor final do seu produto não sofre alterações, R${valor:.2f}')
elif(op == 3):
    valorAdd = (valor + valor * (2 / 100))
    parcela = valorAdd / 5
    print(f'Certo!! 5 vezes de {parcela}. O valor final do seu produto tem uma adição de 2%, ficando R${valorAdd:.2f}')
elif(op == 4):
    valorAdd = (valor + valor * (8 / 100))
    parcela = valorAdd / 10
    print(f'Certo!! 10 vezes de {parcela}. O valor final do seu produto tem uma adição de 8%, ficando R${valorAdd:.2f}')
else: print('Opção invalida!!')
# Escreva um programa que calcule o preço a
# pagar fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o
# tipo de instalação: R para residências, I para
# indústrias e C para comércios.

# Calcule o preço de acordo com a tabela a seguir:
# Tipo           Faixa (kWh)         Preço (R$)  
# Residencial     Até 500             0,40
#                 Acima de 500        0,65
# Comercial       Até 1000            0,55
#                 Acima de 1000       0,60
# Industrial      Até 5000            0,55
#                 Acima de 5000       0,60

print(4 * '-', 'PagEnergy', 4 * '-')

kwh = int(input('Quantos kWm de energia foi consumido? '))

print('')
print('Diga o tipo de instalação:')
print(' R - Residêncial')
print(' C - Comercial')
print(' I - Industrial')

instal = input(': ').upper()

if(instal == 'R'): 
    if(kwh <= 500): 
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
    print(f'Segundo seu gasto de {kwh} kWh e instalação residêncial, o valor a pagar é R${preco}')
elif(instal == 'C'):
    if(kwh <= 1000): 
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
    print(f'Segundo seu gasto de {kwh} kWh e instalação comercial, o valor a pagar é R${preco}')
elif(instal == 'C'):
    if(kwh <= 5000): 
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
    print(f'Segundo seu gasto de {kwh} kWh e instalação industrial, o valor a pagar é R${preco}')
else: print('Valor invalido! Digite: R, C ou I - Maiúsculo')
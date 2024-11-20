# Escreva um programa que pergunte a
# quantidade de km percorridos por um
# carro alugado pelo usuário, assim como a
# quantidade de dias pelos quais o carro foi
# alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$ 60 por dia e R$ 0,15
# por km rodado.

percorrido = int(input('Quantos km você percorreu com o veículo? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

rodado = percorrido * 0.15
diasUsados = dias * 60
total = rodado + diasUsados

print(f'O custo total do uso foi de R${total:.2f}')
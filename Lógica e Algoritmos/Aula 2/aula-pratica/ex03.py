# Desenvolva um algoritmo que solicite ao
# usuário o preço de um produto e um
# percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o
# preço final do produto.

preco = float(input('Digite o preço do produto: '))
perc = float(input('Digite quantos porcento de desconto deseja: '))
desconto = preco * ( perc / 100 )
valorDescontado = preco - desconto

print(f'O valor do produto é R${preco}. O valor pedido de desconto é de {perc}%')
print(f'A desconto calculado foi de R${desconto}. Assim o valor final do produto é R${valorDescontado}')

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

# Crie uma variável de string que receba uma
# frase qualquer. Crie uma segunda variável,
# agora contendo a metade da string digitada.
# Imprima na tela somente os dois últimos
# caracteres da segunda variável do tipo string

s1 = 'testando'
print(len(s1))
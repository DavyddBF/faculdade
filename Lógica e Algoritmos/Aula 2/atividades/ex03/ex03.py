# desenvolva um algoritmo que solicite ao usuário o preço
# de um produto e um percentual de desconto a ser aplicado a ele. Calcule-o e
# exiba o valor do desconto e o preço final do produto.

preco =  float(input('Digite o preço do produto: '))
perc = float(input('Digite quantos porcento de desconto deseja: '))
desconto = preco * ( perc / 100 )
valorDescontado = preco - desconto

print(f'O valor do produto é R${preco}. O valor pedido de desconto é de {perc}%')
print(f'A desconto calculado foi de R${desconto}. Assim o valor final do produto é R${valorDescontado}')
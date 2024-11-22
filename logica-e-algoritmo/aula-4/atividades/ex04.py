# Escreva um algoritmo que calcule a média dos números pares de 1 até
# 100 (1 e 100 inclusos). Implemente o laço usando for

num = 0
qtdLaco = 0

for i in range(1, 100 + 1, 1):
    if(i % 2 == 0):
        num += i
        qtdLaco += 1
        print(i)
    else: continue

media = num / qtdLaco

print(f'Soma dos números pares: {num}')
print(f'A média de números pares é: {media}')
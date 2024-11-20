# desenvolva um algoritmo que solicite ao usuário uma
# quantidade de dias, de horas, de minutos e de segundos. Calcule o total de
# segundos resultante e imprima-o na tela, para o usuário.

dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
min = int(input('Quantos min? '))
seg = int(input('Quantos seg? '))

total = seg + (min * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

res = 'O total de segundo calculados é de %i' % total
print(res)
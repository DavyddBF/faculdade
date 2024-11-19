dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
min = int(input('Quantos min? '))
seg = int(input('Quantos seg? '))

total = seg + (min * 60) + (horas * 60 * 60) + (dias * 24 * 60 * 60)

res = 'O total de segundo calculados é de %i' % total
print(res)
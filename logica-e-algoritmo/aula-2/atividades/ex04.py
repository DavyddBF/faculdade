# desenvolva um algoritmo que converta uma temperatura
# de Celsius (C) em Fahrenheit (F). A equação de conversão é
# F = (9 * C) / 5 + 32

c = int(input('Quanto graus C está? '))
fah = ( 9 * c / 5) + 32
print(f'A temperatudo em Celsius é de {c} graus. Convertendo para Fahrenheit fica em {fah}')
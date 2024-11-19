# desenvolva um algoritmo que solicite ao usuário dois
# números inteiros. Imprima a soma desses dois números na tela.

x = int(input('Digite um número inteiro: '))
y = int(input('Digite um segundo numero inteiro: '))

resForm1 = 'A soma do numero {} e {} é igual a {}'.format(x, y, x+y)
resForm2 = f'A soma do numero {x} e {y} é igual a {x+y}'

print(resForm1)
print(resForm2)
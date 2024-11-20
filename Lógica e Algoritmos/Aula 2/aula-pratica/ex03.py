# Crie uma variável de string que receba uma
# frase qualquer. Crie uma segunda variável,
# agora contendo a metade da string digitada.
# Imprima na tela somente os dois últimos
# caracteres da segunda variável do tipo string

s1 = 'testando'
s2 = s1[:int(len(s1) / 2)]
print(s2[-2:])


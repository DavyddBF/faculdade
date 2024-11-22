# Escreva um algoritmo que obtenha do usuário uma frase de tamanho
# entre 10 e 30 caracteres (faça a validação deste dado).
# Após a frase ter sido digitada corretamente, faça a impressão dela na tela
# da maneira exata como foi digitada e, em seguida, remova os espaços da frase
# e imprima novamente, sem espaços.
# Para resolver este exercício utilize os conhecimentos adquiridos na aula
# 2 (fatiamento e tamanho de strings), bem como o que foi aprendido na seção 4.1
# desta etapa.

frase = input('Digite uma frase de 10 a 30 caracteres!')

while(True):
    if(len(frase) < 10 or len(frase) > 30):
        print(f'Sua frase teve {len(frase)} caracteres...')
        frase = input('Digite uma frase de 10 a 30 caracteres!')
    else: break

print(f'Com espaço: {frase}')
print(f'Sem espaço: ', end = '')
for i in range(0, len(frase)):
    if(frase[i] != ' '):
        print(frase[i], end = '')
# Escreva um algoritmo que repetidamente pergunte ao usuário qual sua
# idade e seu sexo (M ou F). Para cada resposta o programa deve responder
# imprimir a mensagem:
# “Boa noite, Senhor. Sua idade é <IDADE>” caso gênero masculino ou
# “Boa noite, Senhora. Sua idade é <IDADE>” caso gênero feminino.
# O programa deve encerrar quando o usuário digitar uma idade negativa

idade = int(input('Qual é a sua idade? '))

while(idade > 0):
    genero = input('Qual é o seu gênero? (M ou F) ').upper()
    if(genero == 'M'):
        print(f'Boa noite Senhor,  sua idade é {idade}.')
    else:
        if(genero == 'F'):
            print(f'Boa noite Senhora, sua idade é {idade}.')
        else:
            print('Opção inexistente!!')
    idade = int(input('Qual é a sua idade? '))
print('Encerrando...')

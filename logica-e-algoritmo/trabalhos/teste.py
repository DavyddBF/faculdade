# contador = 0
# while True:
#     print('Deseja pedir mais alguma coisa? (sim para continuar / não para cancelar)')
#     op = input(': ').lower()
#     while True:
        
#         if(op == 'sim' or 's'):
#             contador += 30
#             break
#         elif(op == 'não' or op == 'nao' or op == 'n'):
#             break
#         else: 
#             print('Opção inválida!!')
#             continue
#     if(op == 'sim' or  op == 's'):
#         continue
#     else:
#         break
# print('Oi')

contador = 0
while True:
    print('Deseja pedir mais alguma coisa? (sim para continuar / não para cancelar)')
    op = input(': ').lower()
    
    while True:
        if op == 'sim' or op == 's':
            contador += 30
            break  # Sai do loop da pergunta, mas continua no principal
        elif op == 'não' or op == 'nao' or op == 'n':
            break  # Sai do loop da pergunta e não adiciona mais
        else: 
            print('Opção inválida!!')
            op = input(': ').lower()  # Solicita a entrada novamente
            continue  # Continua no loop da pergunta
            
    if op == 'sim' or op == 's':
        continue  # Continua no loop principal
    else:
        break  # Sai do loop principal

print('Oi')

# Elabore um programa em Python que:
#     A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
# Por exemplo: print(“Sistema desenvolvido por Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
#     B. Deve-se implementar o input do valorBase do plano e da idade do cliente [EXIGÊNCIA DE CÓDIGO 2 de 6];
#     C. Deve-se implementar as regras de valores conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
#     D. Deve-se implementar o valorMensal [EXIGÊNCIA DE CÓDIGO 4 de 6];
#     E. Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
#     F. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
#     G. Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
#     H. Deve-se apresentar na saída de console a utilização do sistema informando uma idade maior ou igual a 29 anos, apresentando na saída de console o valorMensal do plano [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  

print('Davyd de Basto Ferreira')
valorBase = float(input('Informe o valor Base do Plano: '))
idade = int(input('Informe o idade do cliente: '))
if idade >= 0 and idade < 19 :
    valorMensal = valorBase * (100 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
elif idade >= 19 and idade < 29 :
    valorMensal = valorBase * (150 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
elif idade >= 29 and idade < 39 :
    valorMensal = valorBase * (225 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
elif idade >= 39 and idade < 49 :
    valorMensal = valorBase * (240 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
elif idade >= 49 and idade < 59 :
    valorMensal = valorBase * (350 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
else:
    valorMensal = valorBase * (600 / 100)
    print('O valor mensal do plano é: %.2f' % valorMensal)
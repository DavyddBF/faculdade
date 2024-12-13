# Enunciado: Você foi contratado para desenvolver um sistema de Venda de uma Empresa Y que vende toras de arvore para outras empresas que vendem madeira. Você ficou com a parte de desenvolver a interface com o cliente.
# A Empresa Y opera as vendas da seguinte maneira:
#     • Tora de Pinho (PIN), o valor do metro cúbico (m³) é de cento e cinquenta reais e quarenta centavos;
#     • Tora de Peroba (PER), o valor do metro cúbico (m³) é de cento e setenta reais e vinte centavos;
#     • Tora de Mogno (MOG), o valor do metro cúbico (m³) é de cento e noventa reais e noventa centavos;
#     • Tora de Ipê (IPE), o valor do metro cúbico (m³) é de duzentos e dez reais e dez centavos; 
#     • Tora de Imbuia (IMB), o valor do metro cúbico (m³) é de duzentos e vinte reais e setenta centavos;

#     • Se a quantidade (em m³) de toras for menor que 100 não há desconto na venda (0/100);
#     • Se a quantidade (em m³) de toras for igual ou maior que 100 e menor que 500, o desconto será de 4% (4/100);
#     • Se a quantidade (em m³) de toras for igual ou maior que 500 e menor que 1000, o desconto será de 9% (9/100);
#     • Se a quantidade (em m³) de toras for igual ou maior que 1000 e menor ou igual que 2000, o desconto será de 16% (16/100);
#     • Se a quantidade (em m³) de toras for maior que 2000, não é aceito pedidos com essa quantidade de toras;
	
#     • Para o adicional de transporte rodoviário (1) é cobrado um valor extra de 1000 reais;
#     • Para o adicional de transporte ferroviário (2) é cobrado um valor extra de 2000 reais;
#     • Para o adicional de transporte hidroviário (3) é cobrado um valor extra de 2500 reais;

# O valor final da conta é calculado da seguinte maneira:

# total = ((tipoMadeira * qtdToras)*(1-desconto)) + transporte

# Elabore um programa em Python que: 
#     A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui). 
# Por exemplo: print(“Bem-vindos a Madeireira do Lenhador Bruno Kostiuk”)  [EXIGÊNCIA DE CÓDIGO 1 de 7];
#     B. Deve-se implementar a função escolha_tipo() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
#         a. Pergunta o tipo de madeira desejado;
#         b. Retorna o VALOR do tipo de madeira com base na escolha do usuário (use return);
#         c. Repete a pergunta do item B.a se digitar uma opção diferente de: PIN/PER/MOG/IPE/IMB;
#     C. Deve-se implementar a função qtd_toras() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
#         a. Pergunta a quantidade de toras;
#         b. Retorna (use return) a quantidade de toras E o valor do desconto (os dois valores) seguindo a regra do enunciado;
#         c. Repete a pergunta do item C.a se digitar um valor acima de 2000 ou valor não numérico (use try/except para não numérico)
#     D. Deve-se implementar a função transporte() que não recebe parâmetros e que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
#         a. Pergunta pelo serviço adicional de transporte;
#         b. Retorna (use return) o valor de apenas uma das opções de transporte;
#         c. Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/3;
#     E. Deve-se implementar o total a pagar no código principal (main), ou seja, não pode estar dentro de função, conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
#     F. Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
#     G. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
#     H. Deve-se apresentar na saída de console uma mensagem com o seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
#     I. Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de tipo de madeira [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
#     J. Deve-se apresentar na saída de console um pedido no qual o usuário digitou um valor que ultrapasse a quantidade máxima de toras aceitas (2000) [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
#     K. Deve-se apresentar na saída de console um pedido com opção de tipo de madeira, quantidade de toras e transporte válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];


# Menu básico
print('Bem-vindos à Madeireira do Lenhador Davyd de Basto Ferreira')

# Escolha do tipo de madeira
while(True):
    print('')
    print('Entre com o Tipo de Madeira desejado')
    print('PIN - Tora de Pinho')
    print('PER - Tora de Peroba')
    print('MOG - Tora de Mogno')
    print('IPE - Tora de Ipê')
    print('IMB - Tora de Imbuia')
    tipo = input('>> ').upper()

    if(tipo == 'PIN'):
        valorMadeira = 150.40
        break
    elif(tipo == 'PER'):
        valorMadeira = 170.20
        break
    elif(tipo == 'MOG'):
        valorMadeira = 190.90
        break
    elif(tipo == 'IPE'):
        valorMadeira = 210.10
        break
    elif(tipo == 'IMB'):
        valorMadeira = 220.70
        break
    else:
        print('Escolha inválida! Entre com o modelo novamente')
        print('')

# Escolhe a quantidade de toras e dita o desconto
while(True):
    try:
        qtdToras = int(input('Digite a quantidade de toras (m³): '))
        if(qtdToras > 2000):
            print('Não aceitamos pedidos com essa quantidade de toras.')
            print('Por favor, entre com a quantidade novamente.')
            print('')
            continue
        elif(qtdToras < 100):
            desconto = 0
        elif(qtdToras < 500):
            desconto = 4 / 100
        elif(qtdToras < 1000):
            desconto = 9 / 100
        else:
            desconto = 16 / 100
        break
    except ValueError:
        print('Entrada inválida! Digite um número inteiro.')

# Menu pra escolher a op de Transporte
print('')
print('Escolha o tipo de Transporte:')
print('1 - Rodoviário  - R$ 1000.00')
print('2 - Ferroviário - R$ 2000.00')
print('3 - Hidroviário - R$ 2500.00')

while(True):
    transporte = input('>> ')
    if(transporte == '1'):
        valorTransporte = 1000.00
        break
    elif(transporte == '2'):
        valorTransporte = 2000.00
        break
    elif(transporte == '3'):
        valorTransporte = 2500.00
        break
    else:
        print('Opção inválida! Tente novamente.')

# Total
total = ((valorMadeira * qtdToras) * (1 - desconto)) + valorTransporte

print(f'Total: R$ {total: .2f}')

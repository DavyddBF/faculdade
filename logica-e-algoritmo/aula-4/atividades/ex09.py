# Escreva um algoritmo que imprima na tela as horas no formato H:M:S
# dentro de um intervalo definido pelo usuário. O usuário deverá delimitar o
# intervalo de horas que deseja imprimir (por exemplo, das 7h até as 14h).
# Valide os dados de entrada para que seu programa só aceite valores
# válidos para hora (de 0 até 23h) e que a hora inicial digitada não seja maior que
# a final. Caso isso aconteça o usuário deverá digitar o intervalo novamente.

hInicial = int(input('Deseja iniciar em qual hora? '))
hFinal = int(input('Deseja terminar em qual hora? '))

while(True):
    if(hInicial > hFinal or hInicial < 0 or hInicial > 23 or hFinal < 0 or hFinal > 23):
        hInicial = int(input('Deseja iniciar em qual hora? '))
        hFinal = int(input('Deseja terminar em qual hora? '))
    else: break

for h in range(hInicial, hFinal + 1, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            print(h, ':', m, ':', s)
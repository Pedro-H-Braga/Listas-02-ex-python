'''
Faça um programa que leia duas coordenadas (X e Y) de um ponto e informe em que quadrante do plano
cartesiano ele está.

quando:
x positivo com y positivo > primeiro quadrante: x > 0 and y > 0 
x negativo com y positivo > segundo quadrante: x < 0 and y > 0
x negativo com y negativo > terceiro quadrante: x < 0 and y < 0
x positivo com y negativo > segundo quadrante: x > 0 and y < 0
x ou y = 0: saia
'''
a = True

while a == True:
    x = float(input("INFORME O 'X': "))
    y = float(input("INFORME O 'Y': "))
    if x > 0 and y > 0:
        print(f"({x};{y}) pertencem ao PRIMEIRO QUADRANTE")
    elif x < 0 and y > 0:
        print(f"({x};{y}) pertencem ao SEGUNDO QUADRANTE")
    elif x < 0 and y < 0:
        print(f"({x};{y}) pertencem ao TERCEIRO QUADRANTE")
    elif x > 0 and y < 0:
        print(f"({x};{y}) pertencem ao QUARTO QUADRANTE")
    else: a = False
    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

print("VOCE ESCOLHEU SAIR DO PROGRAMA")
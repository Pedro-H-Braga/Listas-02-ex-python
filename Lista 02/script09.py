'''
Faça um programa que leia os 3 ângulos de um triângulo e informe o seu tipo:

Triângulo acutângulo ........................: possui todos os ângulos com medidas menores que 90º.
(ang1 e ang2 e ang3) < 90
Triângulo retângulo ...........................: possui um ângulo com medida igual a 90º.
(ang1 ou ang2 ou ang3) == 90
Triângulo obtusângulo ......................: possui um ângulo obtuso, maior que 90º.
(ang1 ou ang2 ou ang3) > 90


'''
a = True

while a == True:
    print("INFORME A SEGUIR OS ANGULOS PARA VERIFICAR A QUE TIPO DE TRIANGULO SE ENCAIXA")

    ang1 = int(input("INFORME O ANGULO 1: "))      
    ang2 = int(input("INFORME O ANGULO 2: "))
    ang3 = int(input("INFORME O ANGULO 3: "))

    if (ang1 and ang2 and ang3) < 90 > 0:
        print(f"({ang1};{ang2};{ang3}) Sao angulos de um --> Triangulo ACUTANGULO <--")
    elif (ang1 or ang2 or ang3) == 90:
        print(f"({ang1};{ang2};{ang3}) Sao angulos de um --> Triangulo RETANGULO <--")
    elif (ang1 or ang2 or ang3) > 90:
        print(f"({ang1}°;{ang2}°;{ang3}°) Sao angulos de um --> Triangulo OBTUSANGULO <--")
    else: print("-----VALOR INFORMADO NÃO CONDIZENTE COM O REQUERIDO-----\nTENTE NOVAMENTE:")

    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

'''
Faça um programa que leia os 3 ângulos de um triângulo e informe o seu tipo:

Triângulo acutângulo ........................: possui todos os ângulos com medidas menores que 90º.
(ang1 e ang2 e ang3) < 90
Triângulo retângulo ...........................: possui um ângulo com medida igual a 90º.
(ang1 ou ang2 ou ang3) == 90
Triângulo obtusângulo ......................: possui um ângulo obtuso, maior que 90º.
(ang1 ou ang2 ou ang3) > 90

• Todos os ângulos devem ser positivos;
• A Soma dos ângulos internos deve ser 180º
'''
a = True

while a == True:
    print("INFORME A SEGUIR OS ANGULOS PARA VERIFICAR A QUE TIPO DE TRIANGULO SE ENCAIXA")

    soma_180 = 180
    
    ang1 = int(input("INFORME O ANGULO 1: "))      
    bkp_180_ang1 = soma_180 - ang1 
    print(f"Falta ({bkp_180_ang1}°) para as somas do angulos serem --> 180° <--")
    ang2 = int(input("INFORME O ANGULO 2: "))
    bkp_180_ang2 = bkp_180_ang1 - ang2
    print(f"Falta ({bkp_180_ang2}°) para as somas do angulos serem --> 180° <--")
    ang3 = int(input("INFORME O ANGULO 3: "))
    bkp_180_ang3 = bkp_180_ang2 - ang3
    print(f"Falta ({bkp_180_ang3}°) para as somas do angulos serem --> 180° <--")
    
    #soma_angulos = ang1 + ang2 + ang3
    # variavel de backup
    # fazer um for para - quando pegar um valor mostrar quanto falta para atingir a soma de 180 - 

    if ((((ang1 and ang2) and ang3) > 0) and ((ang1 + ang2 + ang3) == 180)) == True:
        if ((ang1 and ang2 and ang3) < 90) == True:
            print(f"({ang1};{ang2};{ang3}) Sao angulos de um --> Triangulo ACUTANGULO <--")
        elif (((ang1 or ang2) or ang3) == 90) == True:
            print(f"({ang1};{ang2};{ang3}) Sao angulos de um --> Triangulo RETANGULO <--")
        elif (((ang1 or ang2) or ang3) > 90) == True:
            print(f"({ang1}°;{ang2}°;{ang3}°) Sao angulos de um --> Triangulo OBTUSANGULO <--")
            
        else: print("-----VALOR INFORMADO NÃO CONDIZENTE COM O REQUERIDO-----")
    
    else: print(f"({ang1}°;{ang2}°;{ang3}°) --> VALORES IRREGULARES <-- \nLEMBRE QUE A SOMA DOS ANGULOS TEM QUE SER 180 COM VALORES POSITIVOS")
    
    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

'''
10. Faça um programa que leia os 3 lados de um triângulo e informe o seu tipo:
Triângulo equilátero ..........................: possui os três lados com medidas iguais.
Triângulo isósceles ...........................: possui dois lados com medidas iguais.
Triângulo escaleno............................: possui os três lados com medidas diferentes.
Lembrando que todos os lados devem ser positivos e que:
|𝑏 − 𝑐| < 𝑎 < 𝑏 +𝑐
|𝑎 − 𝑐| < 𝑏 < 𝑎 + 𝑐
|𝑎 − 𝑏| < 𝑐 < 𝑎 + b

ELEVADO AO QUADRADO E DEPOIS FEITO A RAIZ QUADRADA É IGUAL AO MÓDULO DE ALGO
'''
a = True

while a == True:
    print("\nINFORME A SEGUIR OS LADOS PARA VERIFICAR QUAL O TIPO DO TRIANGULO\n")    
    
    lado1 = int(input("INFORME O LADO 1: "))          
    lado2 = int(input("INFORME O LADO 2: "))    
    lado3 = int(input("INFORME O LADO 3: "))        
      
    if (lado1 > 0) and (lado2 > 0) and (lado3 > 0):

        if (lado1 == lado2 == lado3):
            print(f"({lado1};{lado2};{lado3}) Tem TODOS os lados IGUAIS: --> Triangulo EQUILATERO <--")
                    
        elif (lado1 != lado2 != lado3):
            print(f"({lado1};{lado2};{lado3}) Tem UM dos lados DIFERENTE --> Triangulo ESCALENO <--")
    
        else: print(f"({lado1};{lado2};{lado3}) Tem TODOS os lados DIFERENTES --> Triangulo ISOSCELES <--")
            
    else: print("-----VALOR INFORMADO NÃO CONDIZENTE COM O QUE FOI PEDIDO-----")
    
    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

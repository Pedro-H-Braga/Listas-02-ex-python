'''
Faça um programa que leia a coordenada cartesiana de dois pontos e calcule a distância entre eles

FORMULA: dis_ab = RAIZQUADRADA((x_b - x_a)**2 + (y_b - y_a)**2)
raiz quadrada de 4 = 4*pow(1/2)
'''
x_a = float(input("Informe o X do ponto A: "))
x_b = float(input("Informe o X do ponto B: "))

y_a = float(input("Informe o Y do ponto A: "))
y_b = float(input("Informe o Y do ponto B: "))

resultado = ((x_b - x_a)**2 + (y_b - y_a)**2)**(1/2)

print(f"RESULTADO: {resultado}")

'''
Faça um programa que leia dois valores inteiros (A e B) correspondentes aos catetos de um triângulo e
calcule a hipotenusa. Lembrando que a hipotenusa só deverá ser calculada se os valores informados
forem positivos.
'''

a = int(input("informe o cateto A: "))
b = int(input("informe o cateto B: "))

if (a and b) > 0:
    hipotenusa = ((a**2) + (b**2))**(1/2)
    print(f"RESULTADO DA HIPOTENUSA: {hipotenusa}")
else: print("Os valores informados precisam ser POSITIVOS")

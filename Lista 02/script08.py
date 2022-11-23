'''
Faça um programa que leia os valores de a, b e c e calcule as raízes de uma equação do 2º grau.
Lembrando que para ser uma equação do 2º grau, o valor de a não pode ser 0 (zero).
Utilize as fórmulas abaixo:
∆= 𝑏2 − 4𝑎𝑐
𝑥 = −𝑏 ± √∆/2𝑎
Lembrando que:
∆ < 0 → ∄ 𝑥 ∈ ℝ
∆= 0 → ∃ 𝑥 ∈ ℝ | 𝑥1 = 𝑥2
∆ > 0 → ∃ 𝑥 ∈ ℝ | 𝑥1 ≠ 𝑥2
'''
a = True

while a == True:

    a = float(input("INFORME O *A*: "))
    b = float(input("INFORME O *B*: "))
    c = float(input("INFORME O *C*: "))

    if a == 0:
        print("'A' NÃO PODE SER IGUAL A '0'")
        a = False

    delta = (b**2) - (4*a*c)
    #print(delta)
    #𝑥 = −𝑏 ± √∆/2𝑎
    x1 = b-((delta/(2*a))**(1/2))
    print(f'{x1:.2}')
    x2 = b+((delta/(2*a))**(1/2))
    print(f'{x2:.2}')
    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

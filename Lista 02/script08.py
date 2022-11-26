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
operando = True

while operando == True:

    a = float(input("Informe o *A*: "))

    if a == 0:
        print("'A' NÃO PODE SER IGUAL A '0'")
    else:
        b = float(input("Informe o *B*: "))
        c = float(input("Informe o *C*: "))

        delta = (b**2) - (4*a*c)
        
        if delta < 0:
            print(f"{delta} < 0 --> NÃO PERTENCE AOS REAIS")
        elif delta == 0:
            print(f"{delta} = 0 --> TERÁ RAIZES IGUAIS")
        elif delta > 0:
            print(f"{delta} > 0 --> TERÁ RAIZES DIFERENTES")
        else: 
            print("-----VALORES INVALIDOS-----")
            operando = False
        
        x1 = (-b+(delta**0.5)) / (2*a)
        print(f'X1:{x1:.2}')
            
        x2 = (-b-(delta**0.5))/(2*a)
        print(f'X2:{x2:.2}')
        
        operando = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
        if operando == 'SIM':
            operando = True
            print("VOCE ESCOLHEU CONTINUAR")
        else: operando = False

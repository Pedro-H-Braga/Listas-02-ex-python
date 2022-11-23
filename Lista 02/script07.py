print("A MEDIDA EM PESO SERA EM *KG* E A ALTURA EM *METROS*, ex:\npeso: 68.60 & altura: 1.65")


a = True

while a == True:
    peso = float(input('INFORME AQUI O SEU PESO: '))
    altura = float(input('INFORME AQUI SUA ALTURA: '))

    imc = peso/(altura**2)

    if imc < 18.5:
        print(f'SEU PESO FOI: {imc}\nVOCE ESTA ABAIXO DO PESO')
    elif (imc > 18.5) and (imc < 24.9):
        print(f'SEU PESO FOI: {imc}\nSEU PESO ESTA NORMAL')
    elif (imc > 25) and (imc < 29.9):
        print(f'SEU PESO FOI: {imc}\nVOCE ESTA COM SOBREPESO')
    elif (imc > 30) and (imc < 34.9):
        print(f'SEU PESO FOI: {imc}\nVOCE ESTA COM OBESIDADE GRAU I')
    elif (imc > 35) and (imc < 39.9):
        print(f'SEU PESO FOI: {imc}\nVOCE ESTA COM OBESIDADE GRAU II')
    elif imc >= 40:
        print(f'SEU PESO FOI: {imc}\nVOCE ESTA COM OBESIDADE GRAU III OU MORBIDA')
    else: 
        print('INFORME UM VALOR NUMERICO POSITIVO')

    a = input("VOCE QUER FAZER NOVAMENTE? SIM OU NÃO: ")
    if a == 'SIM':
        a = True
        print("VOCE ESCOLHEU CONTINUAR")
    else: a = False

print("VOCE ESCOLHEU SAIR DO PROGRAMA")

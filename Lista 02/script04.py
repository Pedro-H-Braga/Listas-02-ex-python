'''
Faça um programa que leia um valor inteiro e informe se ele é um número par positivo, par negativo,
ímpar positivo, ímpar negativo ou se é nulo.
'''
a = int(input('INFORME UM VALOR INTEIRO: '))

if (a%2==0) and (a > 0):
    print("O valor informado é um PAR POSITIVO")
elif (a%2==0) and (a < 0):
    print("O valor informado é um PAR NEGATIVO")
elif (a%2==1) and (a > 0):
    print("O valor informado é um IMPAR POSITIVO")
elif (a%2==1) and (a < 0):
    print("O valor informado é um IMPAR NEGATIVO")
else: print("NÃO SE ENQUADRA EM NENHUM DOS REQUISITOS")
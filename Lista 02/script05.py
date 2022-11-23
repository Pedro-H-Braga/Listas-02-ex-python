'''
Faça um programa que leia um valor inteiro correspondente a um ano entre 1900 e 2100 e diga se o ano
informado é bissexto ou não.
'''
a = int(input("INFORME UM ANO ENTRE 1900 A 2100 PARA VERIFICAR SE É BISSEXTO OU NÃO: "))

if (a in range(1899,2101)) and (a%4==0):
    print(f"{a} É ANO BISSEXTO")
else: print(f"{a}: ANO INFORMADO NÃO É BISSEXTO")
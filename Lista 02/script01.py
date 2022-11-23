'''
Faça um programa que leia dois valores para as variáveis A e B e efetue a troca dos valores de forma
que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável
A. Apresente os valores trocados.
'''

a = input("digite o valor de A: ")
b = input("digite o valor de B: ")

c = a 
a = b
b = c 

print(f"Valor de A: {a}\nValor de B: {b}")

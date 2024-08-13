'''Exercício 1) Faça um algoritmo que receba um número e apresente a tabuada do mesmo ao final'''

numero = int(input("Digite um número para ver sua tabuada: "))

i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1
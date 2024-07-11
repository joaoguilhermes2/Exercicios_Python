''' 16. Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os 
números ímpares de 1 até N em ordem crescente. ''' 

N = int(input("Digite um número inteiro e ímpar: "))
numero = 0

while N <= 0 or N % 2 == 1:
    N = int(input("Digite um número inteiro e ímpar: "))

while numero <= N:
    print(numero)
    numero += 3
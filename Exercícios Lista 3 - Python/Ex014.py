''' 14. Crie um programa que leia um número inteiro positivo par N e imprima todos os números 
pares de 0 até N em ordem crescente. '''

N = int(input("Digite um número inteiro e par: "))
numero = 0

while N <= 0 or N % 2 != 0:
    N = int(input("Digite um número inteiro e par: "))

while numero <= N:
    print(numero)
    numero += 2
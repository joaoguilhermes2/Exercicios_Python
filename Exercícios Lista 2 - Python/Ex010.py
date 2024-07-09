''' 10. Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre: 
• O número digitado ao quadrado; 
• A raiz quadrada do número digitado; '''

import math
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    quadrado = numero ** 2
    raiz_quadrada = math.sqrt(numero)
    print(f"O  número {numero} ao quadrado é {quadrado}")
    print(f"A raiz quadrada do número {numero} é {raiz_quadrada}")
else:
    print("O número digitado não é positivo!")
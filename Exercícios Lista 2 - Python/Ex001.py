''' 1. Crie um programa que leia 2 números inteiros e 1 real. Calcule e mostre:  o produto do primeiro 
com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro número 
digitado ao cubo. '''

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = float(input("Digite um número real: "))

a = n1 * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3

res = a + b + c

print(f"O produto do primeiro com a metade do segundo é {a}.")
print(f"A soma do triplo do primeiro com o terceiro é {b}.")
print(f"O terceiro cubo digitado ao cubo é {c}.")
print(f"O resultado da soma de todas as operações é {res:.2f}.")
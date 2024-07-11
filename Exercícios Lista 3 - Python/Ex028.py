''' 28. Escreva um programa que calcule e escreva o valor de S:
S = 1 / 1 + 3 / 2 + 5 / 3 + 7 / 4 ... 99 / 50
'''

S = 0
denominador = 1
numerador = 1

while numerador <= 99 and denominador <= 50:
    S += numerador / denominador
    numerador += 2
    denominador += 1

print(f"O valor de S é: {S}")
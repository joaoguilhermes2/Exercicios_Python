''' 24. Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3 
ou 5. '''

limite = 1000
soma = 0
numero = 1

while numero < limite:
    if numero % 3 == 0 or numero % 5 == 0:
        soma += numero
    numero += 1

print(f"A soma de todos os números abaixo de 1000 que são múltiplos de 3 e 5 é: {soma}")
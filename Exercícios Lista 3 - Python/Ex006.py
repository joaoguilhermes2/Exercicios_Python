''' 6. Escreva um programa que peça ao usuário para digitar 10 valores e some-os. '''

soma = 0
contador = 0

while contador < 10:
    valor = int(input("Digite um número: "))
    soma += valor
    contador += 1
    
print(f"A soma de todos os 10 números é de {soma}")
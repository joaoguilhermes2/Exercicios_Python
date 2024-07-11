''' 9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido. ''' 

menor = float('inf')
maior = float('-inf')

contador = 0

while contador < 10:
    numero = int(input("Digite um número: "))
    if numero >= maior:
        maior = numero
    
    if numero <= menor:
        menor = numero

    contador += 1

print(f"O menor valor lido é {menor}")
print(f"O maior valor lido é {maior}")
''' 8. Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua 
média. ''' 

soma = 0
contador = 0

while contador < 10:
    valor = int(input("Digite um número inteiro positivo: "))
    soma += valor
    media = soma / 10
    contador += 1
       
print(f"A média de todos os 10 números inteiros positivos é de {media}")
''' 18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A 
quantidade de números a serem lidos deve será fornecida pelo usuário. '''

cont = 0
lista_numeros = []
quantidade = int(input("Digite a quantidade de números a serem lidos: "))

while cont < quantidade:
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero)
    cont = cont + 1

maior = max(lista_numeros)
print(f"O maior valor entre todos os {quantidade} números é {maior}")
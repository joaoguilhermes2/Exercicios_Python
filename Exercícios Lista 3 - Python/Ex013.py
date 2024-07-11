''' 13. Crie um programa que leia um número inteiro positivo N e imprima todos os números naturais 
de 0 até N em ordem decrescente. '''

contador = 0
soma = 0
numero = int(input("Digite um número: "))

while contador < numero:
    contador += 1
    soma = numero - contador + 1
    print(soma)

print(contador)
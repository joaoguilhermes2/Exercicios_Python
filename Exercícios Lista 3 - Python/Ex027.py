''' 27. Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do 
Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 '''

contador = 1
resultado = 1

A = int(input("Digite um valor: "))

while contador <= A:
    resultado *= contador
    contador += 1

print(f"O resultado de {A}! é: {resultado}")
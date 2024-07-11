''' 17. Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros 
números naturais. '''

contador = 0
soma = 0
numero = int(input("Digite um número inteiro: "))

while contador < numero:
    contador += 1
    soma = soma + contador
    
print(soma)
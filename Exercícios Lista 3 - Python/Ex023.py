''' 23. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse 
número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é: 
1 + 2 + 3 + 6 + 11 + 22 + 33 = 78 ''' 

soma = 0
divisor = 1

numero = int(input("Digite um número inteiro: "))

while divisor <= numero // 2:
    if numero % divisor == 0:
        soma += divisor
    divisor += 1

print(f"A soma dos divisores de {numero} (excluindo ele mesmo) é: {soma}")

''' 12. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim 
como a diferença existente entre ambos. ''' 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O número {n1} é maior que o número {n2}.")
else:
    print(f"O número {n2} é maior que o número {n1}.")
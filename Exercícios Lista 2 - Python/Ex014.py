''' 14. Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem 
crescente. Caso contrário, imprima não está em ordem crescente. ''' 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 < n3:
    print("Crescente")
else:
    print("Não está em ordem crescente")
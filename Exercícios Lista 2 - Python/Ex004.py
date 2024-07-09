''' 4. Crie um programa que receba três números e mostre-os se estão em ordem crescente. ''' 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lsta = [n1, n2, n3]
print(sorted(lsta))
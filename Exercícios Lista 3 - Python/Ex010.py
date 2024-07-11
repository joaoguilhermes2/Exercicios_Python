''' 10. Crie um programa que leia um número inteiro N e depois imprima os N primeiros números 
naturais ímpares. ''' 

n = int(input("Digite um número: "))

i = 1

while i <= (n + n):
    if i % 2 != 0:
        print(i)
        i += 1
    else:
        i += 1
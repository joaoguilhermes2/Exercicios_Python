''' 2. Crie um programa que determine o mostre os 5 primeiros números ímpares, considerando 
números maiores que 0. '''

numero = int(input("Digite um número: "))

i = 1

while i <= (numero + numero):
    if i % 2 != 0:
        print(i)
        i += 1
    else:
        i += 1
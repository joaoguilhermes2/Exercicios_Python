''' 3. Crie um programa que determine o mostre os 10 primeiros números pares, considerando 
números maiores que 0. ''' 

numero = int(input("Digite um número: "))

i = 0

while i <= (numero + numero):
    if i % 2 == 0:
        print(i)
        i += 1
    else:
        i += 1
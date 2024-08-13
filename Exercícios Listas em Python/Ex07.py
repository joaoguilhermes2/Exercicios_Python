'''Exercício 7) Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.'''

n = int(input("Digite o valor de n: "))
num_impar = 1
for i in range(1, n + 1):
    print(i, num_impar)
    num_impar += 2
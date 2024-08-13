'''Exercício 8) Faça para 10 números inteiros para um vetor de inteiros. Computar um segundo vetor que terá o resultado da multiplicação por um escalar inteiro 5.'''

vetor_original = []

for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i+1)))
    vetor_original.append(numero)

vetor_multiplicado = [numero * 5 for numero in vetor_original]

print("Vetor original:", vetor_original)
print("Vetor multiplicado por 5:", vetor_multiplicado)
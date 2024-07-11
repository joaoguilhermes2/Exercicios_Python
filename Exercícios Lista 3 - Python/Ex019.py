''' 19. Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um 
dos algarismos que compõem o número. '''

numero = int(input("Digite um número inteiro entre 100 e 9999: "))
numero_orig = numero
posicao = 0

while numero < 100 or numero > 9999:
    numero = int(input("Digite um número inteiro entre 100 e 9999: "))
while numero > 0:
    digito = numero % 10
    print(f"Digito na posição {posicao}: {digito}")
    numero = numero // 10
    posicao += 1

    print(f"Número original: {numero_orig}")
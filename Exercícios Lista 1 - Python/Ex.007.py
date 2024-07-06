# 7. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.

numero = int(input("Digite um número: "))

sucessor = (numero + 1) * 3
antecessor = (numero - 1) * 2

soma = sucessor + antecessor

print(f"A soma do sucessor ao triplo de {numero} com o seu antecessor ao dobro é: ", soma)
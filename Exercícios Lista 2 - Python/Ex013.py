''' 13. Crie um programa que receba dois números e mostre o maior. Se por acaso, os dois números 
forem iguais, imprima a mensagem: Números iguais. '''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O maior número entre {n1} e {n2}, é {n1}.")
elif n2 > n1:
    print(f"O maior número entre {n1} e {n2}, é {n2}.")
elif n1 == n2:
    print(f"Os números {n1} e {n2} são iguais!")
else:
    print("Número inválido.")
''' 25. Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando 
for informada a idade 0), e calcule a idade média desse grupo. ''' 

contador = 0
soma = 0

while True:
    idade = int(input("Digite sua idade: "))

    if idade == 0:
        break

    contador += 1
    soma += idade

    media = soma / contador

print(f"A média de todas as idades é: {media}")
'''Exercício 4) Faça um algoritmo que receba o número de avaliações do estudante que será (utilizado como contador), após receba as notas e apresente a média do estudante.'''

num_avaliacoes = int(input("Digite o número de avaliações: "))

soma_notas = 0

for i in range(num_avaliacoes):
    nota = float(input(f"Digite a nota da avaliação {i+1}: "))
    soma_notas += nota

media = soma_notas / num_avaliacoes

print(f"A média do estudante é: {media:.2f}")
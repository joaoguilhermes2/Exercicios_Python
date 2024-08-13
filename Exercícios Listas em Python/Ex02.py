'''Exercício 2) Faça um algoritmo que inicialize uma lista de 10 cidades que deseja conhecer e apresente em ordem decrescente (da última para a primeira)'''

cidades = ["Rio de Janeiro", "São Paulo", "Bahia", "Ceará", "Minas Gerais", "Amazonas", "Paraná", "Pernambuco", "Goiás", "Maranhão"]

for i in range(len(cidades) - 1, -1, -1):
    print(cidades[i])
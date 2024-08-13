'''Exercício 5) Crie um programa que receba a palavra FELICIDADE e imprima a posição de cada letra da palavra e informe qual letra está sendo impressa na posição x. Após imprima a mensagem que o programa foi finalizado.'''

palavra = "FELICIDADE"

for indice, letra in enumerate(palavra):
    print(f"Posição {indice} da Lista: {letra}")

print("O programa foi finalizado.")
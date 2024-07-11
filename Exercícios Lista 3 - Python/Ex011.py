''' 11. Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 
primeiros números pares. '''

contador = 0
soma = 0

while contador < 50:
    contador += 1
    soma += contador * 2

print(soma)
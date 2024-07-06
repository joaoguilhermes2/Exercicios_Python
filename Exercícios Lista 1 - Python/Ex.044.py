''' 44. O restaurante a kilo Bem-Bão cobra R$57,00 por cada quilo de refeição. Escreva um algoritmo 
que leia o peso do prato montado pelo cliente (em gramas) e imprima o valor a pagar. Assuma 
que a balança já desconte o peso do prato. '''

peso_grama = float(input("Digite o peso do seu prato em gramas: "))

preco_por_quilo = 57.00
peso_quilos = peso_grama / 1000

valor_total = peso_quilos * preco_por_quilo

print(f"O valor total a pagar é R$ {valor_total}")
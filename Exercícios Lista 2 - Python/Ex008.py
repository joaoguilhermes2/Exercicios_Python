''' 8. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do 
número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido. ''' 

import math
numero = float(input("Digite um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")
else:
    print("O número digitado não é positivo!")
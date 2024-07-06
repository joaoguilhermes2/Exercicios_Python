''' 33. Sejam a e b os catetos de um triâ ngulo, onde a hipotenusa obtida pela equação: ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎 = √ 𝑎2 +𝑏2. 
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa e imprima o resultado dessa operação. '''

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

hipotenusa = (a ** 2) + (a ** 2) 
raiz_quadrada = math.sqrt(hipotenusa)

print(f"O valor da hipotenusa é {raiz_quadrada}")
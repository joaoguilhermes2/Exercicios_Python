''' 41. Calcule as raízes da equação de 2o grau. 
Lembrando que:
∆ = B2−4ac 
E ax2+ bx + c = 0 representa uma equação de 2o grau. 
A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem “Não é equação 
de segundo grau”. 
Se ∆ < 0, não existe real. Imprima a mensagem: Não existe raiz. 
Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única. 
Se ∆ ≥ 0, imprima as duas raízes reais. ''' 

import math

a = 1
b = -3
c = 2

if a == 0:
    print("Não é equação de segundo grau")

delta = b**2 - 4*a*c

if delta < 0:
        print("Não existe raiz")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"Raiz única: {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Raízes: {raiz1} e {raiz2}")
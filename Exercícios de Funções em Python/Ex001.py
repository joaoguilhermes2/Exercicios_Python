''' Crie uma função que necessite de três argumentos, e que 
imprima o produto desses três argumentos. '''

def prod(n1, n2, n3):
    res = (n1 * n2) * n3
    print(f"O resultado da multiplicação de {n1} X {n2} X {n3} é: {res}")

prod(10, 23, 45)
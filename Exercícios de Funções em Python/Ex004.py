''' Escreva um programa, com uma função que necessite de um 
argumento. A função retornar o valor de caractere ‘P’, se 
seu argumento for positivo, e ‘N’, se seu argumento for 
zero ou negativo. '''

def verificar_valor(valor):
    if valor > 0:
        return "P"
    else:
        return "N"

print(verificar_valor(10))
print(verificar_valor(0))
print(verificar_valor(12365))

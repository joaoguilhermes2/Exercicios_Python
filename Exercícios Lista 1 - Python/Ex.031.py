''' 31. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em 
dólares. ''' 

valor = float(input("Digite um valor para converter em dólares: "))

cotacao_dolar = 5.05

conversao = valor * cotacao_dolar

print(f"O valor {valor} convertido em dólares é {conversao} $")
''' 29. Faça leitura de três valores e apresente como resultado a soma dos quadrados dos três valores 
lidos. ''' 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

n1 = n1 ** 2
n2 = n2 ** 2
n3 = n3 ** 2

soma = n1 + n2 + n3

print(f"A soma dos quadrados dos números é {soma}")
''' 9. Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas 
com os valores invertidos. ''' 

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

aux = n1
n1 = n2
n2 = aux

print(f"O valor novo do primeiro número é: {n1}")
print(f"O valor novo do segundo número é: {n2}")
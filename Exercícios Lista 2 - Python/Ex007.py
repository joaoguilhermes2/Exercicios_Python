''' 7. Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor 
de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser 
vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um 
algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda. ''' 

valor_aquisicao = float(input("Digite o valor de aquisição do produto: R$"))

if valor_aquisicao < 50.00:
    valor_venda = valor_aquisicao * 1.45
else:
    valor_venda = valor_aquisicao * 1.3

print(f"O seu valor de venda foi de R$ {valor_venda}")
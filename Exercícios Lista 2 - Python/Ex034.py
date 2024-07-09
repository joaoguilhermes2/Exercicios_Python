''' 34. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e 
escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a 
segunda tabela).
Preço antigo          | Percentual de aumento 
até R$ 50             |          5%                       
entre R$ 50 e R$ 100  |         10% 
acima de R$ 100       |         15%
'''

preco_antigo = float(input("Digite o preço antigo do produto: R$ "))

if preco_antigo <= 50.00:
    valor_novo = preco_antigo + (preco_antigo * 0.10)
    print(f"O novo preço do produto é de {valor_novo:.2f}")
elif preco_antigo > 50.00 and preco_antigo <= 100.00:
    valor_novo = preco_antigo + (preco_antigo * 0.10)
    print(f"O novo preço do produto é de {valor_novo:.2f}")
elif preco_antigo > 100.00:
    valor_novo = preco_antigo + (preco_antigo * 0.10)
    print(f"O novo preço do produto é de {valor_novo:.2f}")
else:
    print("Valor Inválido!")
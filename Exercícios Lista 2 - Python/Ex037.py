''' 37. O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do 
distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, 
de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor. 
Custo de Fábrica                | % do Distribuidor | % dos Impostos
 Até R$12.000,00                |        5          |     isento
 entre R$12.000,00 e 25.000,00  |        10         |       15
 acima de R$25.000,00           |        15         |       20
'''

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

if custo_fabrica <= 12000:
    percentual_distribuidor = 5
    percentual_impostos = 0
elif 12000 < custo_fabrica <= 25000:
    percentual_distribuidor = 10
    percentual_impostos = 15
else:
    percentual_distribuidor = 15
    percentual_impostos = 20

comissao_distribuidor = custo_fabrica * (percentual_distribuidor / 100)
impostos = custo_fabrica * (percentual_impostos / 100)

custo_consumidor = custo_fabrica + comissao_distribuidor + impostos

print(f"O custo ao consumidor do carro é: R$ {custo_consumidor:.2f}")
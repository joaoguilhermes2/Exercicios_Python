''' 39. Crie um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 
litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os 
respectivos preços em 3 situações:  - comprar apenas latas de 18 litros;  - comprar apenas galões de 3,6 litros; '''  

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

cobertura = 6
litros_necessarios = area / cobertura

lata_capacidade = 18
lata_preco = 80.00

galao_capacidade = 3.6
galao_preco = 25.00

latas_quant = lata_preco // lata_capacidade
preco_latas = latas_quant * lata_preco

galoes_quant = galao_preco // galao_capacidade
preco_galoes = galoes_quant * galao_preco

print(f"\nPara pintar uma área de {litros_necessarios} metros quadrados:")
print(f"Comprando apenas latas de 18 litros:")
print(f"Quantidade de latas:{latas_quant}")
print(f"Preço total: R${preco_latas}") 
print(f"\nComprando apenas galões de 3,6 litros:")
print(f"Quantidade de galões:{galoes_quant}")
print(f"Preço total: R${preco_galoes}")
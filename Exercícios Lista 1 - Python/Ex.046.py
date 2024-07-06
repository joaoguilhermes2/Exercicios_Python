''' 46. 4. A lanchonete do Gauchão vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias 
de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de queijo 
ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um algoritmo 
em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as quantidades 
(em quilos) de queijo, presunto e carne necessários para compra. ''' 

quant_sanduiches = int(input("Digite a quantidade de sanduiches que devem ser feitas: "))
fatia_queijo = int(input("Digite a quantidade de fatias de queijo que você deseja colocar no seu sanduíche: "))
fatia_presunto = int(input("Digite a quantidade de fatias de presunto que você deseja colocar no seu sanduíche: "))
carne_hamburguer = int(input("Digite a quantidade de rodelas de hamburguer que você deseja colocar no seu sanduíche: "))

peso_por_queijo = 50 * 2
peso_por_presunto = 50
peso_por_carne_hamburguer = 100

total_queijo = quant_sanduiches * peso_por_queijo
total_presunto = quant_sanduiches * peso_por_presunto
total_carne = quant_sanduiches * peso_por_carne_hamburguer

total_queijo_kg = total_queijo / 1000
total_presunto_kg = total_presunto / 1000
total_carne_kg = total_carne / 1000

print(f"A quantidade necessária de queijo em Kg para comprar é de {total_queijo_kg}")
print(f"A quantidade necessária de presunto em Kg para comprar é de {total_presunto_kg}")
print(f"A quantidade necessária de rodelas de carne em Kg para comprar é de {total_carne_kg}")
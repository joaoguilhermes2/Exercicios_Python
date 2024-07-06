''' 43. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto 
arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de 
poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos para o dono. Com 3 
base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular 
os dados solicitados. '''

quant_paes = int(input("Digite a quantidades de pães vendidos: "))
quant_broa = int(input("Digite a quantidades de broas vendidos: "))

pao = 0.12
broa = 1.50

valor_pao = quant_paes * 0.12
valor_broa = quant_broa * 1.50
valor_total = valor_pao + valor_broa

valor_poup = valor_total * 0.10

print(f"O valor total arrecadado foi de R$ {valor_total}")
print(f"A quantidade guardada na poupança é R$ {valor_poup:.2f}")
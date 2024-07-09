''' 40. Crie um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, Crie um programa que nos dê:  - salário bruto. - quanto pagou ao INSS. - quanto pagou ao sindicato. - o salário líquido. 
calcule os descontos e o salário líquido, conforme a tabela abaixo: 
IR (11%) | INSS (8%) | Sindicato (5 %) 
- Salário Bruto : R$ 
- Salário Líquido: R$ 
Obs.: Salário Bruto - Descontos = Salário Líquido. '''

ganho_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))

salario_bruto = ganho_por_hora + horas_trabalhadas

desconto_ir = 0.11 * salario_bruto
desconto_inss = 0.08 * salario_bruto
desconto_sindicato = 0.05 * salario_bruto

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto IR (11%): R$ {desconto_ir:.2f}")
print(f"Desconto INSS (8%): R$ {desconto_inss:.2f}")
print(f"Desconto Sindicato (5%): R$ {desconto_sindicato:.2f}")
print(f"Total de Descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
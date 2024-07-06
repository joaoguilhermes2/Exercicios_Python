''' 47. Uma Indústria de Peças automotivas paga R$32,50 por hora normal trabalhada, e R$44,50 por 
hora extra. Faça um  algoritmo  que leia a quantidade de horas normais trabalhas e a quantidade 
de horas extras. Calcule e imprima o  salário  bruto  e  o  salário  líquido  de  um  determinado  
funcionário.  Considere  que  o  salário  líquido  é  igual  ao  salário  bruto  descontando-se  11% 
do INSS. '''

horas_normais = float(input("Digite a quantidade de horas trabalhadas: "))
horas_extra = float(input("Digite a quantidade de horas extras trabalhadas: "))

hora_normal_trabalhada = 32.50
hora_extra_trabalhada = 44.50

sal_bruto = (horas_normais * hora_normal_trabalhada) + (horas_extra * hora_extra_trabalhada)

taxa_inss = 0.11
desconto_inss = sal_bruto - taxa_inss

sal_liquido = sal_bruto - desconto_inss

print(f"O salário líquido é de R$ {sal_liquido:.2f}")
print(f"O salário bruto é de R$ {sal_bruto}")
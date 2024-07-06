''' 48. A granja Frangofit possui um controle automatizado de cada frango da sua produção. No pé 
direito  do  frango  há  um  anel  com  um  chip  de  identificação;  no  pé  esquerdo  são  dois  
anéis  para  indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa 
R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja 
para marcar todos os seus frangos. ''' 

custo_chip = 4.00
custo_anel_alimento = 3.00

quant_frangos = int(input("Digite a quantidade de frangos na granja: "))

custo_total_chips = quant_frangos * custo_chip
custo_total_aneis_alimento = (quant_frangos * 2) * custo_anel_alimento

gasto_total = custo_total_chips + custo_total_aneis_alimento

print(f"O gasto total da granja para marcar todos os frangos é de {gasto_total}")
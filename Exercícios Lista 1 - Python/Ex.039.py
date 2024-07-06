''' 39. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas 
no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado. ''' 

hora_trabalho = float(input("Digite o valor da hora de trabalho (em reais): "))
horas_mes = float(input("Digite o número de horas trabalhdas no mês: "))

acumulado = hora_trabalho * horas_mes
porcentagem = acumulado * 0.10
salario = acumulado + porcentagem

print(f"O valor a ser pago para o funcionário é {salario}")
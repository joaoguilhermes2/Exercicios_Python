''' 16. Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários 
acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor 
do seu salário líquido. ''' 

horas_trabalhadas = float(input("Digite o total de horas trabalhadas: "))

valor_hora = 40.50
salario = horas_trabalhadas * valor_hora

if salario > 2500.00:
    imposto = 0.11 * salario
    print(f"O seu salário atual com imposto é de R$ {imposto}")
else:
    print(f"Seu salário sem imposto é de R$ {salario}")
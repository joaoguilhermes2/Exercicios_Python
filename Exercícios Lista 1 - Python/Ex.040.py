''' 40. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que 
esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de 
imposto sobre o salário-base. ''' 

salario_base = float(input("Digite o seu salário: R$ "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_final = (salario_base + gratificacao) - imposto

print(f"O salário base de R$ {salario_base} equivale a salário final de R$ {salario_final}")


''' 38. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o 
número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, 
sabendo-se que são descontados 8% para imposto de renda. ''' 

num_dia_trabalhados = int(input("Digite o número de dias trabalhado: "))

pagamento = (num_dia_trabalhados * 30.00) - 0.08
liquido = (0.08 * pagamento) / 100
quantia_liquida = pagamento - liquido

print(f"O valor que o encanador recebeu foi R${quantia_liquida:.2f}")
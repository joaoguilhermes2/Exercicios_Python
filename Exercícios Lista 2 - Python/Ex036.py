''' 36. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela´ que 
considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários com menor 
salário terão um aumento proporcionalmente maior do que os funcionários com um salário 
maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber um bônus 
adicional de salário. Crie um programa que leia: 
• o valor do salário atual do funcionário; 
• o tempo de serviço desse funcionário na empresa (número de anos de trabalho na 
empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o valor do 
salário final reajustado, ou uma mensagem caso o funcionário não tenha direito a nenhum 
aumento. 
Salário Atual      | Reajuste (%) | Tempo de Serviço | Bônus
 Até 500,00        |     25%      |  Abaixo de 1 ano | Sem bônus
 Até 1000,00       |     20%      |   De 1 a 3 anos  | 100,00
 Até 1500,00       |     15%      |   De 4 a 6 anos  | 200,00
 Até 2000,00       |     10%      |   De 7 a 10 anos | 300,00
 Acima de 2000,00  | Sem reajuste |  Mais de 10 anos | 500,00
'''

sal_atual = float(input("Digite o valor do seu salário atual: R$ "))
temp_servico = float(input("Digite quanto tempo de trabalho você está nessa empresa em anos: "))

if sal_atual <= 500.00 and temp_servico < 1:
    reajuste = sal_atual + (sal_atual * 0.25)
    print(f"O seu salário atualizado fica R$ {reajuste} e sem bônus!")
elif sal_atual <= 1000.00 and temp_servico >= 1 and temp_servico <= 3:
    reajuste = (sal_atual + 100) + (sal_atual * 0.20)
    print(f"O seu salário atualizado fica R$ {reajuste} e com bônus de R$ 100 já adicionado ao salário!")
elif sal_atual <= 1500.00 and temp_servico >= 4 and temp_servico <= 6:
    reajuste = (sal_atual + 200.00) + (sal_atual * 0.15)
    print(f"O seu salário atualizado fica R$ {reajuste} e com bônus de R$ 200 já adicionado ao salário!")
elif sal_atual <= 2000.00 and temp_servico >= 7 and temp_servico <= 10:
    reajuste = (sal_atual + 300.00) + (sal_atual * 0.10)
    print(f"O seu salário atualizado fica R$ {reajuste} e com bônus de R$ 300 já adicionado ao salário!")
elif sal_atual > 2000.00 and temp_servico > 10:
    reajuste = (sal_atual + 500.00) + (sal_atual * 0)
    print(f"O seu salário atualizado fica R$ {reajuste} e com bônus de R$ 500 já adicionado ao salário!")
else:
    print("Valor Inválido")
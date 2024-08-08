''' Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento. Ela tem uma quantia X para dar de entrada, uma taxa de juros é definida pelo banco e a pessoa 
pode escolher o número de parcelas que deseja financiar. Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos. O programa deve solicitar 
ao usuário o valor do veiculo, o valor da entrada, a taxa de juros e a quantidade de parcelas. Além disso, o programa deve exibir o valor total pago, a quantia dos juros pagos e o 
valor de cada parcela. O programa deve apresentar as informações de forma clara e objetiva, facilitando a compreensão por parte do usuário. '''

def simularFinanciamento(valor_veiculo, valor_entrada, taxa_juros, parcelas):
    valor_financiado = valor_veiculo - valor_entrada

    taxa_juros_mensal = taxa_juros / 100
    n = parcelas
    
    if taxa_juros_mensal == 0:
        parcela = valor_financiado / n
    else:
        parcela = (valor_financiado * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** (-n))
    
    valor_total_pago = parcela * n
    juros_pagos = valor_total_pago - valor_financiado

    print(f"Valor do veículo: R$ {valor_veiculo:.2f}")
    print(f"Valor da entrada: R$ {valor_entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Taxa de juros mensal: {taxa_juros:.2f}%")
    print(f"Número de parcelas: {parcelas}")
    print(f"Valor de cada parcela: R$ {parcela:.2f}")
    print(f"Valor total pago: R$ {valor_total_pago:.2f}")
    print(f"Quantia dos juros pagos: R$ {juros_pagos:.2f}")

valor_veiculo = float(input("Digite o valor do veículo: R$ "))
valor_entrada = float(input("Digite o valor da entrada: R$ "))
taxa_juros = float(input("Digite a taxa de juros mensal (%): "))
parcelas = int(input("Digite o número de parcelas: "))

simularFinanciamento(valor_veiculo, valor_entrada, taxa_juros, parcelas)

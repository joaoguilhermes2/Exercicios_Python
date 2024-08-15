while True:
    try:
        custo_carro = float(input("Digite o custo de fábrica do carro: R$ "))

        if custo_carro < 12.000:
            comissao = custo_carro + (custo_carro * 0.5)
            print(f"A comissão total do vendedor é de {comissao} e não é cobrado nenhum imposto!")
        elif custo_carro >= 12.000 and custo_carro <= 25.000:
            comissao = custo_carro + (custo_carro * 0.10)
            imposto = custo_carro + (custo_carro * 0.15)
            print(f"A comissão total do vendedor é de R$ {comissao} e é cobrado um imposto de R$ {imposto}")
        elif custo_carro > 25.000:
            comissao = custo_carro + (custo_carro * 0.15)
            imposto = custo_carro + (custo_carro * 0.20)
            print(f"A comissão total do vendedor é de R$ {comissao} e é cobrado um imposto de R$ {imposto}")
        else:
            print("Valor Inválido!")
    except:
        print("Entrada Inválida, digite novamente")
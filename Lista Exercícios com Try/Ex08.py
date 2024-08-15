while True:
    try:
        valor_aquisicao = float(input("Digite o valor de aquisição do produto: R$"))

        if valor_aquisicao < 50.00:
            valor_venda = valor_aquisicao * 1.45
        else:
            valor_venda = valor_aquisicao * 1.3
        print(f"O seu valor de venda foi de R$ {valor_venda}")
        break

    except:
        print("Entrada Inválida!")


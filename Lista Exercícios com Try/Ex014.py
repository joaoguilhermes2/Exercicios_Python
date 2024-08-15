while True:
    try:
        print("Cardápio:")
        print("Lanche *** Código *** Preço")
        print("Hot Dog - 100 - R$ 12.00")
        print("X-Salada - 102 - R$ 18.50")
        print("X-Bacon - 103 - R$ 25.50")
        print("X-Burguer - 104 - R$ 17.00")
        print("\nBebidas *** Código *** Preço")
        print("Suco de Laranja - 105 - R$ 9.50")
        print("Refrigerante - 106 - R$ 6.00")

        opcao = int(input("\nDigite o código do seu pedido: "))

        if opcao == 100:
            valor_pagar = 12.00
            print(f"O total a pagar é de R$ {valor_pagar}")
        elif opcao == 102:
            valor_pagar = 18.50
            print(f"O total a pagar é de R$ {valor_pagar}")
        elif opcao == 103:
            valor_pagar = 25.50
            print(f"O total a pagar é de R$ {valor_pagar}")
        elif opcao == 104:
            valor_pagar = 17.00
            print(f"O total a pagar é de R$ {valor_pagar}")
        elif opcao == 105:
            valor_pagar = 9.50
            print(f"O total a pagar é de R$ {valor_pagar}")
        elif opcao == 106:
            valor_pagar = 6.00
            print(f"O total a pagar é de R$ {valor_pagar}")
        else:
            print("Código Inválido!")
    except:
        print("Entrada Inválida, digite novamente")
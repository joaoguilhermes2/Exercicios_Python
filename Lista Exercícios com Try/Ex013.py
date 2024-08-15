while True:
    try:
        valor_produto = float(input("Digite o valor do produto: R$ "))
        print("1 - MG")
        print("2 - SP")
        print("3 - RJ")
        print("4 - MS")
        estado_destino = int(input("Selecione o seu estado: "))

        MG = 0.07
        SP = 0.12
        RJ = 0.15
        MS = 0.08

        if estado_destino == 1:
            imposto_mg = valor_produto * MG
            valor_total_mg = valor_produto + imposto_mg
            print(f"O valor total acrescido com imposto é de R$ {valor_total_mg}")
        elif estado_destino == 2:
            imposto_sp = valor_produto * SP
            valor_total_sp = valor_produto + imposto_sp
            print(f"O valor total acrescido com imposto é de R$ {valor_total_sp}")
        elif estado_destino == 3:
            imposto_rj = valor_produto * RJ
            valor_total_rj = valor_produto + imposto_rj
            print(f"O valor total acrescido com imposto é de R$ {valor_total_rj}")
        elif estado_destino == 4:
            imposto_ms = valor_produto * MS
            valor_total_ms = valor_produto + imposto_ms
            print(f"O valor total acrescido com imposto é de R$ {valor_total_ms}")
        else:
            print("Opção Inválida!")
    except:
        print("Entrada Inválida, digite novamente!")

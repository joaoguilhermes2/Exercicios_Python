while True:
    try:
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        opcao = int(input("Escolha a opção que deseja realizar: "))

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if opcao == 1:
            soma = num1 + num2
            print(f"A soma entre {num1} e {num2} é igual a {soma}")
        elif opcao == 2:
            subtracao = num1 - num2
            print(f"A subtração entre {num1} e {num2} é igual a {subtracao}")
        elif opcao == 3:
            multiplicacao = num1 * num2
            print(f"A multiplicação entre {num1} e {num2} é igual a {multiplicacao}")
        elif opcao == 4:
            divisao = num1 / num2
            print(f"A divisão entre {num1} e {num2} é igual a {divisao}")
        else:
            print("Opção Inválida!")
    except:
        print("Entrada Inválida, digite novamente!")
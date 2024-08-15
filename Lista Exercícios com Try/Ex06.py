while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        n3 = int(input("Digite o terceiro número: "))

        lsta = [n1, n2, n3]
        print(sorted(lsta))
        break

    except:
        print("Entrada Inválida, digite novamente!")
while True:
    try:
        numero = float(input("Digite um número: "))

        if numero >= 0:
            raiz_quadrada = numero ** 2
            print(f"A raiz quadrada de {numero} é {raiz_quadrada}.")
            break
        else:
            print("O número digitado não é positivo!")

    except:
        print("Entrada Inválida, digite novamente!")
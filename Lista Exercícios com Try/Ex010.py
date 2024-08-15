while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = (nota1 + nota2) / 2

        if nota1 >= 0.0 and nota1 <= 10.00 and nota2 >= 0.0 and nota2 <= 10.00:
            print(f"A média das notas é {media}")
            break
        else:
            print("Uma ou mais notas inválidas")

    except:
        print("Entrada Inválida, digite novamente!")
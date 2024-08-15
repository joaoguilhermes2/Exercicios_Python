while True:
    try:
        a = int(input("Digite o primeiro lado do triângulo: "))
        b = int(input("Digite o segundo lado do triângulo: "))
        c = int(input("Digite o terceiro lado do triângulo: "))

        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                print("Triângulo Equilátero!")
            elif a == b or b == a or a == c or c == a:
                print("Triângulo Isósceles!")
            elif a != b != c or b != a != c or c != b != a:
                print("Triângulo Escaleno!")
            else:
                print("Valor Inválido!")
    except:
        print("Entrada Inválida, digite novamente")
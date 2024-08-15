while True:
    try:
        primeiro = int(input("Digite o primeiro número: "))
        segundo = int(input("Digite o segundo número: "))
        break
    except:
        print("Entrada Inválida, por favor tente novamente!")

if primeiro > segundo:
    print(f"O {primeiro} é o maior número!")
else:
    print(f"O {segundo} é o maior número!")
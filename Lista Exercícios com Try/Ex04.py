while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except:
         print("Você não digitou um número inteiro válido. Tente novamente.")

if numero > 10:
    print("É maior que 10!")
else:
    print("É menor que 10!")
soma = 0
contador = 0

while contador < 10:
    try:
        valor = int(input("Digite um número: "))
        soma += valor
        media = soma / 10
        contador += 1
    except:
        print("Entrada Inválida!")

print(f"A média de todos os 10 números é de {media}")
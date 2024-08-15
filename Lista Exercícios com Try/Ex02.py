menor = float('inf')
maior = float('-inf')

contador = 0

while contador < 10:
    try:
        numero = int(input("Digite um número: "))
        if numero >= maior:
            maior = numero
        
        if numero <= menor:
            menor = numero

        contador += 1
    except:
        print("Entrada Inválida!")

print(f"O menor valor lido é {menor}")
print(f"O maior valor lido é {maior}")
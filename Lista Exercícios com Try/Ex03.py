contador_total = 0
contador_pares = 0

while True:
    try:
        numero = int(input("Digite um número inteiro (0 para sair): "))
        
        if numero == 0:
            break
        
        contador_total += 1
        
        if numero % 2 == 0:
            contador_pares += 1
    except:
        print("Entrada Inválida!")

print(f"Número de dados lidos: {contador_total}")
print(f"Número de valores pares: {contador_pares}")

''' 20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
informado o número de dados lidos e número de valores pares. O processo termina quando for 
digitado o número 0. '''

contador_total = 0
contador_pares = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break
    
    contador_total += 1
    
    if numero % 2 == 0:
        contador_pares += 1

print(f"Número de dados lidos: {contador_total}")
print(f"Número de valores pares: {contador_pares}")

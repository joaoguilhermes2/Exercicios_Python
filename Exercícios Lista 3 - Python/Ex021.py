''' 21. Crie um programa que receba dois números. Calcule e mostre: 
• a soma dos números pares desse intervalo de números, incluindo os números digitados; 
• a multiplicação dos números ímpares desse intervalo, incluindo os digitados; ''' 

soma_pares = 0
multiplicacao_num_impares = 1

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

num = numero1

while num <= numero2:
    if num % 2 == 0:
        soma_pares += num
    else:
        multiplicacao_num_impares *= num
    num += 1

print(f"Soma dos números pares no intervalo: {soma_pares}")
print(f"Multiplicação dos números ímpares no intervalo: {multiplicacao_num_impares}")
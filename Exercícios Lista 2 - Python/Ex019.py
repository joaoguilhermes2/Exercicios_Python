''' 19. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma 
de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se 
o número lido não for maior do que zero, o programa termina com a mensagem “Número 
inválido”. '''

numero = int(input("Digite um número inteiro: "))
dig1 = int(input("Digite o primeiro dígito do numero inserido: "))
dig2 = int(input("Digite o segundo dígito do numero inserido: "))
dig3 = int(input("Digite o terceiro dígito do numero inserido: "))

valor_digitos = dig1 + dig2 + dig3

if numero > 0:
    print(f"O número {numero} corresponde ao valor {valor_digitos} ({dig1} + {dig2} + {dig3}).")
else:
    print("Número Inválido!")
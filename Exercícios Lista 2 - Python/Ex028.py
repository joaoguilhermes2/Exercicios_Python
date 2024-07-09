''' 28. Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu 
de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os 
dois números recebidos. Escreva uma mensagem de erro se a opção for inválida. 
Escolha a opção: 
1- Soma de 2 números. 
2- Diferença entre 2 números (maior pelo menor). 
3- Produto entre 2 números. 
4- Divisão entre 2 números (o denominador não pode ser zero). '''

print("1- Soma de 2 número")
print("2- Diferença entre 2 números")
print("3- Produto entre 2 números")
print("4- Divisão entre 2 números")
opcao = int(input("Escolha a opção: "))

num1 = float(input("Digite um número: "))
num2 = float(input("Digite um outro número: "))

if opcao == 1:
    soma = num1 + num2
    print(f"A soma entre {num1} e {num2} é {soma}")
elif opcao == 2:
    subtracao = num1 - num2
    print(f"A diferença entre {num1} e {num2} é {subtracao}")
elif opcao == 3:
    produto = num1 * num2
    print(f"O produto entre {num1} e {num2} é {produto}")
elif opcao == 4:
    divisao = num1 / num2
    print(f"A divisão entre {num1} e {num2} é {divisao}")
else:
    print("Opção Inválida!")
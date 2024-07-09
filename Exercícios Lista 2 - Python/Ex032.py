''' 32. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes 
categorias: 
Categoria |  Idade 
Infantil  |  5 a 12 
Juvenil   |  12 a 17 
Sênior    |  maiores de 18 anos ''' 

idade = int(input("Digite a sua idade: "))

if idade >= 5 and idade <= 12:
    print("Você é um nadador infantil")
elif idade >= 12 and idade <= 17:
    print("Você é um nadador Juvenil")
elif idade >= 18:
    print("Você é um nadador Sênior")
else:
    print("Número Inválido")
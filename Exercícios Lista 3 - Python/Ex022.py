''' 22. Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de 
notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente 
média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não 
fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido 
como nota de aprovação. ''' 

cont = 0
soma_notas = 0
quantidade = int(input("Digite a quantidade de notas que será informada: "))

while cont < quantidade:
    pontuacao = float(input(f"Digite a nota {cont + 1} (Nota máxima é até 10): "))
    if pontuacao < 0 or pontuacao > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        continue
    soma_notas += pontuacao
    cont += 1

if cont > 0:
    media = soma_notas / cont
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")

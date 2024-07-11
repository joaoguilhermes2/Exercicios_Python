''' 29. Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20? 
Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem 
sobrar resto. ''' 

numero = 20

while True:
    divisivel_por_todos = True
    for i in range(1, 21):
        if numero % i != 0:
            divisivel_por_todos = False
            break
        numero += 20
    
    if divisivel_por_todos:
        print(f"O menor número divisível por todos os números de 1 a 20 é: {numero}")
        break
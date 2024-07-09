''' 22. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente 
a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante. ''' 

numero = int(input("Digite um número entre 1 e 7 (1-Domingo / 2- Segunda-Feira / 3- Terça-Feira / 4- Quarta-Feira / 5- Quinta-Feira / 6- Sexta-Feira / 7- Sábado): "))

if numero == 1:
    print("Hoje é Domingo!")
elif numero == 2:
    print("Hoje é Segunda-Feira!")
elif numero == 3:
    print("Hoje é Terça-Feira!")
elif numero == 4:
    print("Hoje é Quarta-Feira!")
elif numero == 5:
    print("Hoje é Quinta-Feira!")
elif numero == 6:
    print("Hoje é Sexta-Feira!")
elif numero == 7:
    print("Hoje é Sábado!")
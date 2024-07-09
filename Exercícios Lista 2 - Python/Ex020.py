''' 20. Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda 
prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno 
foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos. '''

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

# 1 e 2 nota tem peso "1" e a 3 nota tem peso "2"

media_ponderada = (nota1 + nota2 + (nota3 * 2)) / 3

if media_ponderada >= 60:
    print("Aprovado!")
else:
    print("Reprovado!")
''' 21. A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 
até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; 
Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela 
se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi 
aprovado. Crie todas as verificações necessárias. '''

nota_lab = float(input("Digite a primeira nota: "))
nota_semestral = float(input("Digite a segunda nota: "))
nota_exame = float(input("Digite a terceira nota: "))

# Trabalho Lab. = "Peso 2" / Avaliação Semestral = "Peso 3" / Exame Final = "Peso 5"

peso_lab = 2
peso_semestral = 3
peso_exame = 5

media_final = (nota_lab * peso_lab) + (nota_semestral * peso_semestral) + (nota_exame * peso_exame) / 3

if media_final >= 0.0 and media_final <= 2.9:
    print("Você está reprovado")
elif media_final >= 3.0 and media_final <= 5.9:
    print("Você está de recuperação")
elif media_final >= 6.0:
    print("Aprovado!")
else:
    print("Número Inválido")
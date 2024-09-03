class Aluno:
    def __init__(self,nome,idade,n1,n2,n3,n4):
        self.nome = nome
        self.idade = idade
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def getDados(self):
        print(f"{self.nome} tem {self.idade}")

    def mostrarSituation(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        if media < 4.0:
            return "REPROVADO"
        elif media >= 4.0 and media < 5.9:
            return "EXAME"
        else:
            return "REPROVADO"

aluno = Aluno("Juliana",17,8,7.5,9,8.5)
print("Boletim da Juliana:")
print("Nome:",aluno.nome)
print("Nota 1:",aluno.n1)
print("Nota 2:",aluno.n2)
print("Nota 3:",aluno.n3)
print("Nota 4:",aluno.n4)

situacao = aluno.mostrarSituation()
print(f"Situação da {aluno.nome} é:",situacao)
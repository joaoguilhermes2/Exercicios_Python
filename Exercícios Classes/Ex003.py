class Aluno:
    def __init__(self,nome,RA,n1,n2,n3,n4):
        self.nome = nome
        self.RA = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrar_situacao(self):
        media = (self.n1 + self.n2 + self.n3 + self.n4) / 4
        if media < 0 and media >= 7:
            situacao = "APROVADO"
        elif media >= 5 and media <= 6.9:
            situacao = "EXAME"
        else:
            situacao = "REPROVADO"

        print(f"O aluno {self.nome} com média de {media:.2f} está {situacao}")
        return situacao
    
aluno = Aluno("João",20203456723,8,8,6,5)
aluno.mostrar_situacao()
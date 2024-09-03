class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def mostrarDados(self):
        print(self.matricula)
        print(self.nome)
        print(self.idade)

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)

    def mostrarSituation(self):
        media = sum(self.notas) / len(self.notas)
        if media < 4.0:
            return "REPROVADO"
        elif media >= 4.0 and media < 5.9:
            return "EXAME"
        else:
            return "REPROVADO"

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade,fomacao,disciplina,ch):
        super().__init__(matricula, nome, idade)
        self.formacao = fomacao
        self.disciplina = disciplina
        self.ch = ch

p1 = Professor(456,"Thiago",28,"Análise de Sistemas","Algoritmos",40)
p1.mostrarDados()

aluno1 = Aluno(555,"João",18,[5,9,8,7])
aluno1.mostrarDados()

nota = aluno1.mostrarDados()
print(nota)
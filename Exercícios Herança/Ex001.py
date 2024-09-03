class Filme:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration

    def play(self):
        print(f"O filme {self.name} possui {self.duration} de duração e foi iniciado...")

class FilmeAcao(Filme):
    def __init__(self, name, duration):
        super().__init__(name, duration)

    def explode(self,explosion):
        print(f"Ativar {explosion} 3...2...1...BOOMMMM!!!")

class FilmeDrama(Filme):
    def __init__(self, name, duration):
        super().__init__(name, duration)

    def toCry(self, crying):
        print(f"Estou {crying} ele morreu no dorama...")

class FilmeSuspense(Filme):
    def __init__(self, name, duration):
        super().__init__(name, duration)
    
    def fright(self, scared):
        print(f"Estou {scared} com o filme {self.name}")


filme1 = Filme("Era do Gelo","2h35")
filme1.play()

filme2 = FilmeAcao("RAMBO",185)
filme2.explode("EXPLOSÂO GIGANTE")

filme3 = FilmeDrama("Dorama",200)
filme3.toCry("CHORANDO")

filme4 = FilmeSuspense("Panic 2",150)
filme4.fright("AHHHHH QUE SUSTO")
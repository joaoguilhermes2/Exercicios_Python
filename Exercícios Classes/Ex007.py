class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = (self.ladoA + self.ladoB + self.ladoC)
        return perimetro
    
    def getMaiorLado(self):
        if self.ladoA > self.ladoB or self.ladoC:
            return "LADO A MAIOR"
        elif self.ladoB > self.ladoA or self.ladoC:
            return "LADO B MAIOR"
        else:
            return "LADO C MAIOR"
        
tri1 = Triangulo(35,45,23)
print("LADO A:",tri1.ladoA)
print("LADO B:",tri1.ladoB)
print("LADO C:",tri1.ladoC)
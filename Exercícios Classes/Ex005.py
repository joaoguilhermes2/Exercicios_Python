class Circulo:
    PI = 3.14159

    def __init__(self, raio):
        self.raio = raio

    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def calcular_area(self):
        area = Circulo.PI * (self.raio ** 2)
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 * Circulo.PI * self.raio
        return circunferencia
    
circulo = Circulo(5)
circulo.imprimir_raio()
print(f"Área: {circulo.calcular_area():.2f}")
print(f"Circunferência: {circulo.calcular_circunferencia():.2f}")
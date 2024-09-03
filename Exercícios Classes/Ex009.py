class Carro:
    def __init__(self,marca,modelo,cor,ano,valor,nivel=5):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.nivel = nivel
        self.consumo = 8
        self.valor = valor
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def calculaImpsoto(self):
        imposto = self.valor * 0.025
        return imposto
    
    def abastecer(self,quant):
        self.nivel += quant

    def verificarNIvel(self):
        return self.nivel
    
    def andar(self,km):
        litros = km / self.consumo
        self.nivel -= litros
        print("Consumo...",litros)
    
car1 = Carro("BMW","Fusca","Azul",2001,1235000,2)
print("Marca:",car1.marca)
print("Modelo:",car1.modelo)
print("Cor:",car1.cor)
print("Ano:",car1.ano)
print("Valor:",car1.valor)
print("Nível:",car1.nivel)

car1.ligar()
car1.desligar()

imp = car1.calculaImpsoto()
print(imp)

car1.abastecer(30)
print(car1.verificarNIvel())
car1.andar(65)
class Transporte:
    def __init__(self, capacidade, velocidade_maxima):
        self.capacidade = capacidade
        self.velocidade_maxima = velocidade_maxima

    def mostrar_informacoes(self):
        return f"Capacidade: {self.capacidade} passageiros, Velocidade Máxima: {self.velocidade_maxima} km/h"

class Terrestre(Transporte):
    def __init__(self, capacidade, velocidade_maxima, tipo_terreno):
        super().__init__(capacidade, velocidade_maxima)
        self.tipo_terreno = tipo_terreno

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Tipo de Terreno: {self.tipo_terreno}"

class Automovel(Terrestre):
    def __init__(self, capacidade, velocidade_maxima, tipo_terreno, combustivel):
        super().__init__(capacidade, velocidade_maxima, tipo_terreno)
        self.combustivel = combustivel

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Combustível: {self.combustivel}"

class Aereo(Transporte):
    def __init__(self, capacidade, velocidade_maxima, alcance):
        super().__init__(capacidade, velocidade_maxima)
        self.alcance = alcance

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Alcance: {self.alcance} km"

class AviaoMonomotor(Aereo):
    def __init__(self, capacidade, velocidade_maxima, alcance, tipo_motor):
        super().__init__(capacidade, velocidade_maxima, alcance)
        self.tipo_motor = tipo_motor

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Tipo de Motor: {self.tipo_motor}"

class AviaoComercial(Aereo):
    def __init__(self, capacidade, velocidade_maxima, alcance, numero_assentos):
        super().__init__(capacidade, velocidade_maxima, alcance)
        self.numero_assentos = numero_assentos

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Número de Assentos: {self.numero_assentos}"

class Aquatico(Transporte):
    def __init__(self, capacidade, velocidade_maxima, tipo_propulsao):
        super().__init__(capacidade, velocidade_maxima)
        self.tipo_propulsao = tipo_propulsao

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Tipo de Propulsão: {self.tipo_propulsao}"

class Lancha(Aquatico):
    def __init__(self, capacidade, velocidade_maxima, tipo_propulsao, comprimento):
        super().__init__(capacidade, velocidade_maxima, tipo_propulsao)
        self.comprimento = comprimento

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Comprimento: {self.comprimento} metros"

class Navio(Aquatico):
    def __init__(self, capacidade, velocidade_maxima, tipo_propulsao, carga_maxima):
        super().__init__(capacidade, velocidade_maxima, tipo_propulsao)
        self.carga_maxima = carga_maxima

    def mostrar_informacoes(self):
        return f"{super().mostrar_informacoes()}, Carga Máxima: {self.carga_maxima} toneladas"

automovel1 = Automovel(5, 180, "Asfalto", "Gasolina")
print(automovel1.mostrar_informacoes())

aviao1 = AviaoMonomotor(4, 300, 1000, "Motor a Pistão")
print(aviao1.mostrar_informacoes())

lancha1 = Lancha(10, 80, "Hélice", 15)
print(lancha1.mostrar_informacoes())

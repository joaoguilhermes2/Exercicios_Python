class Imovel:
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.IPTU = IPTU

    def obterParcelaIPTU(self, num_parcelas=1):
        return self.IPTU / num_parcelas
    
    def setValorAluguel(self, novo_valor):
        self.valor_aluguel = novo_valor
    
class ImovelCasa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU, piscina, sala_de_estar):
        super().__init__(inscricao_municipal, valor_aluguel, IPTU)
        self.piscina = piscina
        self.sala_de_estar = sala_de_estar

    def dadosCasa(self):
        print(f"Casa - Inscrição Municipal: {self.inscricao_municipal}, Valor do Aluguel: {self.valor_aluguel}, IPTU: {self.IPTU}, Piscina: {self.piscina}, Sala de Estar: {self.sala_de_estar} m²")

class ImovelCondominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU, quartos):
        super().__init__(inscricao_municipal, valor_aluguel, IPTU)
        self.quartos = quartos

    def dadosCondominio(self):
        print(f"Condomínio - Inscrição Municipal: {self.inscricao_municipal}, Valor do Aluguel: {self.valor_aluguel}, IPTU: {self.IPTU}, Quartos: {self.quartos}")

class ImovelApartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU, churrasqueira):
        super().__init__(inscricao_municipal, valor_aluguel, IPTU)
        self.churrasqueira = churrasqueira

    def dadosApartamento(self):
        print(f"Apartamento - Inscrição Municipal: {self.inscricao_municipal}, Valor do Aluguel: {self.valor_aluguel}, IPTU: {self.IPTU}, Churrasqueira: {self.churrasqueira}")

class ImovelTerreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU, area_m2):
        super().__init__(inscricao_municipal, valor_aluguel, IPTU)
        self.area_m2 = area_m2

    def dadosTerreno(self):
        print(f"Terreno - Inscrição Municipal: {self.inscricao_municipal}, Valor do Aluguel: {self.valor_aluguel}, IPTU: {self.IPTU}, Área: {self.area_m2} m²")

class ImovelChacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, IPTU, elevador, area_de_lazer):
        super().__init__(inscricao_municipal, valor_aluguel, IPTU)
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer

    def dadosChacara(self):
        print(f"Chácara - Inscrição Municipal: {self.inscricao_municipal}, Valor do Aluguel: {self.valor_aluguel}, IPTU: {self.IPTU}, Elevador: {self.elevador}, Área de Lazer: {self.area_de_lazer} m²")

imovel1 = ImovelCasa(234132, 3500.0, 180.0, "Sim", 50)
imovel1.dadosCasa()
print()
imovel2 = ImovelCondominio(234132, 3500.0, 180.0, 3)
imovel2.dadosCondominio()
print()
imovel3 = ImovelApartamento(234132, 3500.0, 180.0, "Sim")
imovel3.dadosApartamento()
print()
imovel4 = ImovelTerreno(345678, 1500.0, 100.0, 500)
imovel4.dadosTerreno()
print()
imovel5 = ImovelChacara(4555555, 1000.0, 200.0, 3, 2)
imovel5.dadosChacara()

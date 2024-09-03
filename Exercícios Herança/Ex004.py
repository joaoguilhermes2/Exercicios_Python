class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def alterarPreco(self,novo_preco):
        self.preco = novo_preco
    
    def escolherAssento(self):
        return self.assento
    
class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"Abastecendo o ônibus com a placa {self.placa}...")

class PassagemAviao(Passagem):
    def __init__(self, preco, assento, portaodeembarque, checkin):
        super().__init__(preco, assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin

    def decolar(self):
        print(f"Decolando do portão {self.portaodeembarque} daqui 10 horas...")

passagem_bus = PassagemBus(150.0, "12A", "ABC1234", True)
print(f"Preço do ônibus: {passagem_bus.preco}")
print(f"Assento do ônibus: {passagem_bus.escolherAssento()}")
passagem_bus.abastecer()

passagem_aviao = PassagemAviao(500.0, "24B", "D5", True)
print(f"Preço do avião: {passagem_aviao.preco}")
print(f"Assento do avião: {passagem_aviao.escolherAssento()}")
passagem_aviao.decolar()

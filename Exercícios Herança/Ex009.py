class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0

    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        return self.valor_total

class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_valor_com_desconto(self):
        valor_com_desconto = self.calcular_valor_total() * (1 - self.desconto / 100)
        return valor_com_desconto

class Parcelada(Compra):
    def __init__(self, numero, produto, valor, num_parcelas):
        super().__init__(numero, produto, valor)
        self.num_parcelas = num_parcelas

    def calcular_valor_parcela(self):
        valor_total = self.calcular_valor_total()
        valor_parcela = valor_total / self.num_parcelas
        return valor_parcela

compra1 = Avista(1, "Notebook", 3000, 10)  # 10% de desconto
print(f"Valor total à vista com desconto: R${compra1.calcular_valor_com_desconto():.2f}")

compra2 = Parcelada(2, "Smartphone", 2000, 5)  # 5 parcelas
print(f"Valor de cada parcela: R${compra2.calcular_valor_parcela():.2f}")

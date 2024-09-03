class NF:
    def __init__(self,numero,tipo,serie,cnpj,razao_social,data,valor_produtos,icms,frete,ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0
        self.calcularValorTotal()

    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social

    def calcularValorTotal(self):
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi

nf = NF(12345,'Entrada',1,'12345678000195','Empresa XYZ','2024-08-29',1000.0,100.0,50.0,30.0)
print(nf.obterNumero())
print(nf.obterDataEmissao())
print(nf.valor_total)
nf.alterarRazaoSocial('Nova Razão Social')
print(nf.razao_social)
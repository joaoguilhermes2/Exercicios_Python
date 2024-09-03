class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterarPreco(self,novo_preco):
        self.preco = novo_preco

    def mostrarSetor(self):
        return self.setor
    
class IngressoVip(Ingresso):
    def __init__(self, preco, setor, camarote, open_bar, open_food, est):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.est = est

    def pegarBebida(self):
        if self.open_bar:
            print("BEBIDA LIBERADA COM SUCESSO")
        else:
            print("COMPRAR FICHAS - STATUS OPENBAR: ",self.open_bar)

    def acessarCamarote(self):
        if self.camarote:
            print("ACESSO LIBERADO")
        else:
            print("VAZA!",self.camarote)
    
sepultura = Ingresso(150,"COMERCIANTES")

sepultura.mostrarSetor()
print(sepultura.preco)
sepultura.alterarPreco(230)
print(sepultura.preco)

vip = IngressoVip(400,"A",False,True,True,True)
vip.pegarBebida()
vip.acessarCamarote()
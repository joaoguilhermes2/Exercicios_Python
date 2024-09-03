class Brinquedos:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f"Estou brincando com o {self.nome} agora!")

class BrinquedosAcao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, arma):
        super().__init__(nome, cor, tamanho, preco)
        self.arma = arma

    def atacar(self):
        print(f"O {self.nome} atacou a barbie com uma {self.arma}!!!")

class BrinquedosTerror(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, faca):
        super().__init__(nome, cor, tamanho, preco)
        self.faca = faca

    def assustar(self):
        print(f"O {self.nome} assustou a barbie com sua faca {self.faca}!!!")

class BrinquedosDrama(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, serie):
        super().__init__(nome, cor, tamanho, preco)
        self.serie = serie

    def chorar(self):
        print(f"O {self.nome} chora quando assiste um {self.serie}!!!")

class BrinquedosFiccao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, viajem):
        super().__init__(nome, cor, tamanho, preco)
        self.viajem = viajem

    def viajar(self):
        print(f"O {self.nome} viajou para {self.viajem}!!!")

class BrinquedosIlustrativos(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, musica):
        super().__init__(nome, cor, tamanho, preco)
        self.musica = musica

    def ouvir(self):
        print(f"O {self.nome} fala enquanto toca uma música da {self.musica} para a criança!!!")

class BrinquedosAcao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, arma):
        super().__init__(nome, cor, tamanho, preco)
        self.arma = arma

    def atacar(self):
        print(f"O {self.nome} atacou a barbie com uma {self.arma}!!!")

class BrinquedosTerror(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, faca):
        super().__init__(nome, cor, tamanho, preco)
        self.faca = faca

    def assustar(self):
        print(f"O {self.nome} assustou a barbie com sua faca {self.faca}!!!")

class BrinquedosDrama(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, serie):
        super().__init__(nome, cor, tamanho, preco)
        self.serie = serie

    def chorar(self):
        print(f"O {self.nome} chora quando assiste um {self.serie}!!!")

class BrinquedosFiccao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, viajem):
        super().__init__(nome, cor, tamanho, preco)
        self.viajem = viajem

    def viajar(self):
        print(f"O {self.nome} viajou para {self.viajem}!!!")

class BrinquedosIlustrativos(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, musica):
        super().__init__(nome, cor, tamanho, preco)
        self.musica = musica

    def ouvir(self):
        print(f"O {self.nome} fala enquanto toca uma música da {self.musica} para a criança!!!")

brinquedo_acao = BrinquedosAcao("Buzz Lightyear","azul","1 metro e 30 cm",560.0,"AK47")
brinquedo_acao.atacar()
print()
brinquedo_terror = BrinquedosTerror("Pânico","preto",180,1200.0,"Tramontina")
brinquedo_terror.assustar()
print()
brinquedo_drama = BrinquedosDrama("Hong Hock","preto",180,1200.0,"Dorama")
brinquedo_drama.chorar()
print()
brinquedo_ficcao = BrinquedosFiccao("The Rock","preto",180,1200.0,"Ao Centro da Terra")
brinquedo_ficcao.viajar()
print()
brinquedo_ilustrativo = BrinquedosIlustrativos("Galinha Pintadinha","amarelo",180,1200.0,"Anitta")
brinquedo_ilustrativo.ouvir()
print()
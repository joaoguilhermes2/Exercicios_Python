class Pessoa:
    def __init__(self,telefone,email,endereco):
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"Hoje chamei o João do telefone: {self.telefone}, e-mail: {self.email} e endereço: {self.endereco} para negociar a moto dele.")

class PessoaFisica(Pessoa):
    def __init__(self, telefone, email, endereco, CPF, CNPJ):
        super().__init__(telefone, email, endereco)
        self.CPF = CPF
        self.CNPJ = CNPJ
    
    def negociar(self):
        print(f"Hoje chamei o Guilherme do telefone: {self.telefone}, e-mail: {self.email}, endereço: {self.endereco}, CPF: {self.endereco} e CNPJ: {self.CNPJ} para negociar a moto dele.")

    def comprar(self):
        print(f"Vou comprar meu computador hoje, so falta colocar meu {self.CPF} e o meu {self.CNPJ}")

class PessoaJuridica(Pessoa):
    def __init__(self, telefone, email, endereco, CPF, CNPJ):
        super().__init__(telefone, email, endereco)
        self.CPF = CPF
        self.CNPJ = CNPJ

    def negociar(self):
        print(f"Hoje chamei a Gabrielle do telefone: {self.telefone}, e-mail: {self.email}, endereço: {self.endereco}, CPF: {self.CPF} e CNPJ: {self.CNPJ} para negociar a moto dele.")

    def investir(self):
        print(f"Vou investir na bolsa de valores, vou colocar meu {self.email}, meu {self.telefone} e o meu {self.endereco} pra finalizar o cadastro!")

pessoa = Pessoa(99999999,"joao@gmail.com.en","Rua da Rupia")
print(f"Telefone do João: {pessoa.telefone}")
print(f"E-mail do João: {pessoa.email}")
print(f"Endereço do João: {pessoa.endereco}")
pessoa.negociar()
print()
pessoa_fisica = PessoaFisica(12345678,"guilher@12me.com.br","Rua do Judas",23446375188,23450)
print(f"Telefone do Guilherme: {pessoa_fisica.telefone}")
print(f"E-mail do Guilherme: {pessoa_fisica.email}")
print(f"Endereço do Guilherme: {pessoa_fisica.endereco}")
print(f"CPF do Guilherme: {pessoa_fisica.CPF}")
print(f"CNPJ do Guilherme: {pessoa_fisica.CNPJ}")
pessoa_fisica.negociar()
pessoa_fisica.comprar()
print()
pessoa_juridica = PessoaJuridica(13572468,"gab@lle.com.br","Rua Dom Aquino",45632178945,56349)
print(f"Telefone do Gabrielle: {pessoa_juridica.telefone}")
print(f"E-mail do Gabrielle: {pessoa_juridica.email}")
print(f"Endereço do Gabrielle: {pessoa_juridica.endereco}")
print(f"CPF do Gabrielle: {pessoa_juridica.CPF}")
print(f"CNPJ do Gabrielle: {pessoa_juridica.CNPJ}")
pessoa_juridica.negociar()
pessoa_juridica.investir()
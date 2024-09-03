class AlunoAcad:
    def __init__(self,nome,idade,peso,altura,mensalidade=120):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade
    
    def calcularIMC(self):
        imc = self.peso / (self.altura * self.altura)
        return imc
    
    def calcularDesconto(self):
        if self.idade < 18:
            desconto = self.mensalidade - (self.mensalidade * 0.20)
            return desconto
        else:
            return self.mensalidade
        
pessoa = AlunoAcad("João",18,75.5,1.80,90)
print(f"Conta Aluno {pessoa.nome}:")
print("Idade:",pessoa.idade)
print("Peso:",pessoa.peso)
print("Altura:",pessoa.altura)
print("Mensalidade:",pessoa.mensalidade)
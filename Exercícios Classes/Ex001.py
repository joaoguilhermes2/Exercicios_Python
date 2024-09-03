class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_nome(self):
        return self.nome

    def alterar_idade(self, idade_nova):
        self.idade = idade_nova
    
    def imprimir_endereco(self):
        return self.endereco
    
dados = Pessoa("João","18 anos","Rua Dom Aquino")
print("Os dados da Pessoa são: ")
print("Nome:",dados.nome)
print("Idade antes da alteração:",dados.idade)

dados.alterar_idade("25 anos")
print("Idade após a alteração:",dados.idade)

print("Endereço:",dados.endereco)

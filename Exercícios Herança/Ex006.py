class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def baterPonto(self):
        self.pontos.append(1)
        
    def mostrarPontos(self):
        return self.pontos
    
    def dadosUsuario(self):
        print(f"Hoje fechei minha meta, o ultimo atendimento que fechei foi do: {self.nome}, da matrícula: {self.matricula}, salário: {self.salario}")

class FuncionarioVendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao

    def baterMeta(self):
        print(f"Hoje tive uma comissão de {self.comissao} R$")

class FuncionarioGerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha

    def verifSenha(self):
        print(f"Minha nova senha para ter acesso ao banco é: {self.senha}")

fucionario = Funcionario("João Guilherme",202027687,1500.0)
print(f"Nome: {fucionario.nome}")
print(f"Matrícula: {fucionario.matricula}")
print(f"Salário: {fucionario.salario}")
fucionario.baterPonto()
print(f"Pontos: {fucionario.mostrarPontos()}")
fucionario.dadosUsuario()
print()
funcionario_vendedor = FuncionarioVendedor("Gabriel",202134501,1200.0,50)
print(f"Nome: {funcionario_vendedor.nome}")
print(f"Matrícula: {funcionario_vendedor.matricula}")
print(f"Salário: {funcionario_vendedor.salario}")
print(f"Comissão: {funcionario_vendedor.comissao}")
funcionario_vendedor.baterMeta()
print()
funcionario_gerente = FuncionarioGerente("Lucas",201920423,7500.0,12457800)
print(f"Nome: {funcionario_gerente.nome}")
print(f"Matrícula: {funcionario_gerente.matricula}")
print(f"Salário: {funcionario_gerente.salario}")
print(f"Senha: {funcionario_gerente.senha}")
funcionario_gerente.verifSenha()
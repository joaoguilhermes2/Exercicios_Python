class Conta:
    def __init__(self, nome, cpf, numero, saldo_inicial):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def imprimir_saldo(self):
        print(f"Saldo atual da conta {self.numero}: R${self.saldo:.2f}")

conta = Conta(nome="João Silva", cpf="123.456.789-00", numero="001", saldo_inicial=1000.00)
conta.imprimir_saldo()
conta.depositar(500.00)
conta.imprimir_saldo()
conta.sacar(200.00)
conta.imprimir_saldo()
conta.sacar(1500.00)
conta.depositar(-50.00)

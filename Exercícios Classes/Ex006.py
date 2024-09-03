class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
        if not self.validar_data():
            raise ValueError("Data inválida")

    def validar_data(self):
        if not (1 <= self.mes <= 12):
            return False
        
        if self.mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= self.dia <= 31
        
        if self.mes in [4, 6, 9, 11]:
            return 1 <= self.dia <= 30
        
        if self.mes == 2:
            if (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0):
                return 1 <= self.dia <= 29
            else:
                return 1 <= self.dia <= 28
        
        return False

    def anotar_tarefa(self, anotacao):
        self.anotacao = anotacao

    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print(f"Não há anotações para {self.dia}/{self.mes}/{self.ano}")

try:
    agenda = Agenda(29, 2, 2024)
    agenda.anotar_tarefa("Reunião com o time.")
    agenda.mostrar_anotacao()
except ValueError as e:
    print(e)

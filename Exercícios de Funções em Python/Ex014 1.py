''' Crie uma função que receba como argumento a potência elétrica de determinado aparelho e o tempo ligado e retorne o consumo em KWh em seguida chame outra função para calcular a 
conta de energia, levando em consideração o  consumo e o valor do KWh como argumentos. '''

def calcular_consumo(potencia, tempo_ligado):
    consumo_kwh = (potencia / 1000) * tempo_ligado
    return consumo_kwh

def calcular_custo(consumo_kwh, valor_kwh):
    custo_total = consumo_kwh * valor_kwh
    return custo_total

potencia = 2000
tempo_ligado = 50
valor_kwh = 1.45

consumo = calcular_consumo(potencia, tempo_ligado)
print(f"Consumo de energia em KWh é de: {consumo:.2f}")

custo = calcular_custo(consumo, valor_kwh)
print(f"Custo total da energia é de: R$ {custo:.2f}")
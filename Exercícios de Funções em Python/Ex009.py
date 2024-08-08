''' O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, a principal função do sistema é calcularTempo(). Considere o valor mínimo de 
R$9,00 por hora e R$ 1,50 por hora adicional. O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. Caso o usuário fique no 
estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado. '''

def calcularTempo(minutos):
    TARIFA_MINIMA = 9.00
    TARIFA_ADICIONAL = 1.50
    MINUTOS_LIMITE = 15
    MINUTOS_POR_HORA = 60

    PIS_ALIQUOTA = 0.0033
    COFINS_ALIQUOTA = 0.0020
    ICMS_ALIQUOTA = 0.17

    if minutos < MINUTOS_LIMITE:
        return 0.00, 0.00, 0.00, 0.00, 0.00

    horas = minutos / MINUTOS_POR_HORA
    
    if horas <= 1:
        valor_total = TARIFA_MINIMA
    else:
        horas_adicionais = horas - 1
        horas_adicionais_cobradas = int(horas_adicionais) if horas_adicionais == int(horas_adicionais) else int(horas_adicionais) + 1
        valor_total = TARIFA_MINIMA + (horas_adicionais_cobradas * TARIFA_ADICIONAL)
    
    pis = valor_total * PIS_ALIQUOTA
    cofins = valor_total * COFINS_ALIQUOTA
    icms = valor_total * ICMS_ALIQUOTA
    impostos = pis + cofins + icms

    valor_com_impostos = valor_total + impostos

    return valor_total, pis, cofins, icms, impostos

tempo_em_minutos = float(input("Digite o tempo utilizado em minutos: "))
valor_total, pis, cofins, icms, impostos = calcularTempo(tempo_em_minutos)

print(f"Tempo {tempo_em_minutos / 60:.0f} horas")
print(f"PIS R$ {pis:.2f}")
print(f"COFINS R$ {cofins:.2f}")
print(f"ICMS R$ {icms:.2f}")
print(f"Impostos R$ {impostos:.2f}")
print(f"Total R$ {valor_total:.2f}")



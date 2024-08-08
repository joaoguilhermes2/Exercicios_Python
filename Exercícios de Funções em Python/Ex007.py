''' Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago conforme o número de horas trabalhadas. Considere a carga horária de 40h por semana como 
salário base, caso ultrapasse o limite de 40h, o funcionário deve receber 50% a mais por hora excedente. '''

def cal_salario(horas_trabalhadas, salario_base_semanal):
    carga_horaria_padrao = 40

    if horas_trabalhadas <= carga_horaria_padrao:
        # Salário base se as horas não ultrapassam o padrão
        salario = salario_base_semanal * (horas_trabalhadas / carga_horaria_padrao)
    else:
        # Salário base para as primeiras 40 horas
        salario_base = salario_base_semanal
        # Horas extras
        horas_extras = horas_trabalhadas - carga_horaria_padrao
        # Valor da hora extra (50% a mais)
        valor_hora_extra = salario_base_semanal / carga_horaria_padrao * 1.5
        # Salário total
        salario = salario_base + (horas_extras * valor_hora_extra / 1.5)
    
    return salario

salario_base_semanal = 1000
horas_trabalhadas = 45

salario = cal_salario(horas_trabalhadas, salario_base_semanal)
print(f"Salário a ser pago: R$ {salario:.2f}")

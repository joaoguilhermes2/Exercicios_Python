''' Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do MS 
(50 Kg) deve pagar uma multa de R$ 4,00 por quilo excedente. O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. Gravar na variável excesso a 
quantidade de quilos além do limite e na variável multa o valor da multa que o pescador deverá pagar. Imprima os dados do programa com as mensagens adequadas. '''

def calcular_multa(quantidade_peixes):
    LIMITE = 50
    VALOR_MULTA = 4.00

    excesso = quantidade_peixes - LIMITE

    if excesso > 0:
        multa = excesso * VALOR_MULTA
        print(f"Quantidade de peixes: {quantidade_peixes} Kg")
        print(f"Excesso: {excesso} Kg")
        print(f"Multa a pagar: R$ {multa:.2f}")
    else:
        print(f"Quantidade de peixes: {quantidade_peixes} Kg")
        print("Não há excesso. Sem multa.")

quantidade_peixes = float(input("Digite a quantidade de peixes (em Kg): "))
calcular_multa(quantidade_peixes)

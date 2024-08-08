''' Um comerciante possui uma loja de artigos de R$ 1,99. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele 
desenvolveu uma tabela que contém o número de itens que o 
cliente comprou e ao lado o valor da conta. Desta forma a 
atendente do caixa precisa apenas contar quantos itens o cliente 
está levando e olhar na tabela de preços. Você foi contratado 
para desenvolver uma função que monta esta tabela de preços, 
que conterá os preços de 1 até 50 produtos, conforme o exemplo 
abaixo: 
    Lojas Quase Dois - Tabela de Preços
    1 - R$ 1.99
    2 - R$ 3.98
    ...
    50 - R$ 99.50 '''

def tabela_precos(quantidade_max):
    preco_unitario = 1.99
    tabela_precos = []
    
    for quantidade in range(1, quantidade_max + 1):
        valor_total = quantidade * preco_unitario
        tabela_precos.append((quantidade, valor_total))
    
    return tabela_precos

def imprimir_tabela_precos(tabela_precos):
    print("Quantidade | Preço")
    print("---------------------")
    for quantidade, preco in tabela_precos:
        print(f"{quantidade:10} | {preco:.2f}")

quantidade_max = 50

tabela_precos = tabela_precos(quantidade_max)
imprimir_tabela_precos(tabela_precos)

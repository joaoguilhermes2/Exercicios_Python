''' Uma rede de churrascaria realiza promoções semanais e precisa automatizar os 
descontos de acordo com o dia da semana (terça-feira 10%, quarta-feira 15%, 
quinta-feira 20%). Crie uma função que calcule o preço final do consumo por 
pessoa. Considere a taxa de atendimento e o couvert, caso o cliente concorde 
com o pagamento. Utilize argumentos nomeados **kwargs, Exemplo de chamada da 
função: desconto(‘quinta-feira’,valor=99.90,taxa=0.10,couvert=15). 

Conta S/ Taxas: 79.92
Conta C/ Taxas:
 Rodízio: 79.92
 Taxa Serviço: 7.99
 Couvert: 15
 TOTAL R$: 102.91 '''

def desconto(dia_da_semana, **kwargs):
    descontos = {
        'terça-feira': 0.10,
        'quarta-feira': 0.15,
        'quinta-feira': 0.20
    }
    
    desconto_porcentagem = descontos.get(dia_da_semana.lower(), 0.0)
    
    valor = kwargs.get('valor', 0.0)
    
    valor_com_desconto = valor * (1 - desconto_porcentagem)
    
    taxa = kwargs.get('taxa', 0.0)
    
    couvert = kwargs.get('couvert', 0.0)
    
    taxa_servico = valor_com_desconto * taxa
    
    total = valor_com_desconto + taxa_servico + couvert
    
    print(f"Conta S/ Taxas: {valor:.2f}")
    print(f"Conta C/ Taxas:")
    print(f" Rodízio: {valor:.2f}")
    print(f" Taxa Serviço: {taxa_servico:.2f}")
    print(f" Couvert: {couvert:.2f}")
    print(f" TOTAL R$: {total:.2f}")

desconto('quinta-feira', valor=99.90, taxa=0.10, couvert=15)

''' 41. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre: 
• o total a pagar com desconto de 10%; 
• o valor de cada parcela, no parcelamento de 3× sem juros; 
• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto) 
• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total) ''' 

valor_total = float(input("Digite o valor total a pagar: R$"))

desconto = valor_total - (valor_total * 0.10)
valor_por_parcela = valor_total / 3
comissao_vista = desconto * 0.05
comissao_parcelada = valor_total * 0.05

print(f"O valor de R$ {valor_total} com desconto fica R$ {desconto}")
print(f"O valor de R$ {valor_total} parcelado em 3x fica R$ {valor_por_parcela}")
print(f"O valor de R$ {valor_total} com uma comissão de venda à vista fica R$ {comissao_vista}")
print(f"O valor de R$ {valor_total} com uma comissão de venda parcelada fica R$ {comissao_parcelada}")
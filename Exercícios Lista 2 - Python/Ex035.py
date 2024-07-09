''' 35. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga ao 
vendedor. Para calcular a comissão, considere a tabela abaixo: 
Venda Mensal                                           | Comissão 
Maior ou igual a R$100.000,00                          | R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R%80.000,00  | R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00   | R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00   | R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00   | R$500,00 + 14% das vendas
Mneor que R$20.000,00                                  | R$400,00 + 14% das vendas
'''
valor_venda = float(input("Digite o valor da venda: R$ "))

if valor_venda >= 100.000:
    comissao = 700.00 + 0.16
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
elif valor_venda < 100.000 and valor_venda >= 80.000:
    comissao = 650.00 + 0.14
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
elif valor_venda < 80.000 and valor_venda >= 60.000:
    comissao = 600.00 + 0.14
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
elif valor_venda < 60.000 and valor_venda >= 40.000:
    comissao = 550.00 + 0.14
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
elif valor_venda < 40.000 and valor_venda >= 20.000:
    comissao = 500.00 + 0.14
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
elif valor_venda < 20.000:
    comissao = 400.00 + 0.14
    print(f"O valor da comissão que deverá ser paga para o vendedor é de R$ {comissao}")
else:
    print("Valor Inválido")

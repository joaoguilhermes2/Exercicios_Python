''' 33. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e 
a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a 
cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão 
abaixo: 
Especificação   | Código | Preço  
Hot Dog         |  100   |  12.00 
X-Salada        |  102   |  18.50 
X-BACON         |  103   |  25.50 
X-Burguer       |  104   |  17.00 
Suco de Laranja |  105   |   9.50 
Refrigerante    |  106   |   6.00'''

print("Cardápio:")
print("Lanche *** Código *** Preço")
print("Hot Dog - 100 - R$ 12.00")
print("X-Salada - 102 - R$ 18.50")
print("X-Bacon - 103 - R$ 25.50")
print("X-Burguer - 104 - R$ 17.00")
print("\nBebidas *** Código *** Preço")
print("Suco de Laranja - 105 - R$ 9.50")
print("Refrigerante - 106 - R$ 6.00")

opcao = int(input("\nDigite o código do seu pedido: "))

if opcao == 100:
    valor_pagar = 12.00
    print(f"O total a pagar é de R$ {valor_pagar}")
elif opcao == 102:
    valor_pagar = 18.50
    print(f"O total a pagar é de R$ {valor_pagar}")
elif opcao == 103:
    valor_pagar = 25.50
    print(f"O total a pagar é de R$ {valor_pagar}")
elif opcao == 104:
    valor_pagar = 17.00
    print(f"O total a pagar é de R$ {valor_pagar}")
elif opcao == 105:
    valor_pagar = 9.50
    print(f"O total a pagar é de R$ {valor_pagar}")
elif opcao == 106:
    valor_pagar = 6.00
    print(f"O total a pagar é de R$ {valor_pagar}")
else:
    print("Código Inválido!")
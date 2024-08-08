''' Escreva um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem 
e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. Por fim deve retornar o novo valor para o usuário 
considerando o percentual do imposto. '''

def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_final = custo + imposto
    return custo_final

taxaImposto = 20.00
custo = 100.00

custo_final = somaImposto(taxaImposto, custo)
print(f"O custo final do item é: R$ {custo_final}")
''' 30. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma 
taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa 
em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço 
final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado 
não for válido, mostrar uma mensagem de erro. ''' 

valor_produto = float(input("Digite o valor do produto: R$ "))
print("1 - MG")
print("2 - SP")
print("3 - RJ")
print("4 - MS")
estado_destino = int(input("Selecione o seu estado: "))

MG = 0.07
SP = 0.12
RJ = 0.15
MS = 0.08

if estado_destino == 1:
    imposto_mg = valor_produto * MG
    valor_total_mg = valor_produto + imposto_mg
    print(f"O valor total acrescido com imposto é de R$ {valor_total_mg}")
elif estado_destino == 2:
    imposto_sp = valor_produto * SP
    valor_total_sp = valor_produto + imposto_sp
    print(f"O valor total acrescido com imposto é de R$ {valor_total_sp}")
elif estado_destino == 3:
    imposto_rj = valor_produto * RJ
    valor_total_rj = valor_produto + imposto_rj
    print(f"O valor total acrescido com imposto é de R$ {valor_total_rj}")
elif estado_destino == 4:
    imposto_ms = valor_produto * MS
    valor_total_ms = valor_produto + imposto_ms
    print(f"O valor total acrescido com imposto é de R$ {valor_total_ms}")
else:
    print("Opção Inválida!")

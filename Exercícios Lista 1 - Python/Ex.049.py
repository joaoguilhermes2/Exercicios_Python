''' 49. A  fábrica  de  refrigerantes Frutuba  vende  seu  produto  em  três  formatos:  lata  de  350  ml,  
garrafa  de  600  ml  e  garrafa  de  2  litros.  Se um comerciante compra  uma  determinada  
quantidade  de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele 
comprou. ''' 

tamanho_lata = 350
tamanho_garrafa_600ml = 600
tamanho_garrafa_2l = 2000

quantidade_latas = int(input("Digite a quantidade de latas de 350ml: "))
quantidade_garrafas_600ml = int(input("Digite a quantidade de garrafas de 600ml: "))
quantidade_garrafas_2l = int(input("Digite a quantidade de garrafas de 2 litros: "))

total_litros = (quantidade_latas * tamanho_lata + 
                quantidade_garrafas_600ml * tamanho_garrafa_600ml +
                quantidade_garrafas_2l * tamanho_garrafa_2l) / 1000

print("O total de litros de refrigerante comprados é:", total_litros, "litros")

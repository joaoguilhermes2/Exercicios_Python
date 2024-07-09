''' 31. Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um 
percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo: 
Consumo   | (Km/L) | Mensagem 
menor que |    8   | Venda o Carro!
entre     | 8 e 14 | Econômico!
maior que |    12  | Super Econômico! '''

distancia = int(input("Digite a distância percorrida em Km: "))
litro_gasolina = int(input("Digite a quantidade de litros consumidos: "))

km_l = distancia / litro_gasolina

if km_l < 8:
    print("Venda o carro!")
elif km_l == 8 and 14:
    print("Econômico!")
elif km_l > 12:
    print("Super Econômico!")
else:
    print("Não é econômico!")
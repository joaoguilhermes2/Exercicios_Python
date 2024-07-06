''' 50. DESAFIO – Utilize a fórmula de Euclides para Calcular a distância entre dois pontos:  
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, 
respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos 
devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo 
plano. Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima 
longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto. ''' 

x1 = float(input("Digite a coordenada de x do primeiro valor: "))
x2 = float(input("Digite a coordenada de x do segundo valor: "))
y1 = float(input("Digite a coordenada de y do primeiro valor: "))
y2 = float(input("Digite a coordenada de y do segundo valor: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

if distancia >= 10:
    print("Longe!")
else:
    print("Perto!")

print(f"{distancia:.2f}")
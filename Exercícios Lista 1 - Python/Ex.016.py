''' 16. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão 
é: M = K / 1.61, sendo K a distância em quilômetros e M em milhas. '''

distancia_quilometros = float(input("Digite a distância em quilômetros: "))

Milhas = distancia_quilometros / 1.61

print(f"A distância em quilometros {distancia_quilometros} convertida em Milhas é {Milhas:.2f}")
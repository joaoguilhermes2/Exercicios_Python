''' 32. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área 
do círculo é:  π ∗ raio2, considere π = 3.141592. '''

raio = float(input("Digite o raio do círculo: "))

area_circulo = 3.141592 * (raio * raio)

print(f"A area do círculo é {area_circulo:.2f}")
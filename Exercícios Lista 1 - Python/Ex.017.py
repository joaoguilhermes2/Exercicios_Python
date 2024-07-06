''' 17. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é:               
R = G ∗ π/180, sendo G o angulo em graus é R em radianos e π = 3.14. '''

angulo_graus = int(input("Digite um ângulo em graus: "))

Radianos = (angulo_graus * 3.14) / 180

print(f"O ângulo {angulo_graus} convertido em radianos é {Radianos:.2f}")
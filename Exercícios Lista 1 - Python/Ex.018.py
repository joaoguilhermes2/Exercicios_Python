''' 18. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:               
G = R ∗180/π, sendo G o angulo em graus é R em radianos e π = 3.14. '''

radiano = float(input("Digite o ângulo em radiano: "))

Grau = (radiano * 180) / 3.14

print(f"O ângulo em radiano {radiano} convertido em graus é {Grau:.2f}")
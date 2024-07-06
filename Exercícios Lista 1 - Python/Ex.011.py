''' 11. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de 
conversão é: C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin. '''

Kelvin = float(input("Digite a temperatura em Kelvin: "))

Celsius = Kelvin - 273.15

print(f"A temperatura em Kelvin {Kelvin} convertida em Graus Celsius é {Celsius}")
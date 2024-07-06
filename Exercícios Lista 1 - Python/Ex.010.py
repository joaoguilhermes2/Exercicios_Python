''' 10. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula 
de conversão é: C = 5.0∗(F −32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em 
Fahrenheit. '''

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

Celsius = 5.0 * (fahrenheit - 32.0) / 9.0

print(f"A temperatura em Fahrenheit{fahrenheit} convertida em Graus Celsius é {Celsius}")
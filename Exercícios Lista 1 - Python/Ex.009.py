''' 9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula 
de conversão é: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura 
em Celsius. '''

temperatura_celsius = float(input("Digite a temperatura em Graus Celsius: "))

Fahrenheit = temperatura_celsius * (9.0 / 5.0) + 32.0

print(f"A temperatura em Graus Celsius {temperatura_celsius} convertida em Fahrenheit é {Fahrenheit}")
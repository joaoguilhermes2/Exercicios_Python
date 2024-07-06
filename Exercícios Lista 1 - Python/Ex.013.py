''' 13. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros 
por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s. '''

velocidade = float(input("Digite a velocidade em km/h: "))

Metros_segundo = velocidade / 3.6

print(f"A velocidade {velocidade} em km/h convertida para m/s é {Metros_segundo}")
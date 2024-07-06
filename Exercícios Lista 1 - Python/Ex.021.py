''' 21. Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. A fórmula de 
conversão é:  L = 1000∗ M, sendo L o volume em litros e M o volume em metros cúbicos. '''

volume = int(input("Digite o volume em metros cúbico: "))

litro = 1000 * volume

print(f"O volume {volume} em metros cúbicos convertido em litros é {litro}")
''' 22. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. A fórmula de 
conversão é: M = L / 1000, sendo L o volume em litros e M o volume em metros cúbicos. ''' 

litro = int(input("Digite o volume em litros: "))

metro = litro / 1000

print(f"O volume {litro} em litros convertido em metros cúbico é {metro:.0f}")
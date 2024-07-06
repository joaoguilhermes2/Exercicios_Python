''' 24. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de 
conversão é:  K = L∗0.45, sendo K a massa em quilogramas e L a massa em libras. '''

massa_libras = float(input("Digite o valor da massa em libras: "))

kilograma = massa_libras * 0.45

print(f"O valor da massa {massa_libras} em libras convertido em quilogramas é {kilograma}")
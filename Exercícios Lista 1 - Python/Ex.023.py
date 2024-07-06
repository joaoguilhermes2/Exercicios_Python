''' 23. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de 
conversão é: L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras. ''' 

massa_quilo = float(input("Digite o valor da massa em quilogramas: "))

libra = massa_quilo / 0.45

print(f"O valor da massa em quilogramas {massa_quilo} convertido em libras é {libra}")
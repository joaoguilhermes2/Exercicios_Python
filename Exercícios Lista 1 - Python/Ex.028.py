''' 28. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2. 
A fórmula de conversão é:  M = H ∗10000, sendo M a área em metros quadrados é H a área em 
hectares. ''' 

hectares = float(input("Digite a área em hectares: "))

metro = hectares * 10000

print(f"O valor da área {hectares} em hectares convertido em metros é {metro}")
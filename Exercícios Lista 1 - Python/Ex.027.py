''' 27. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares. A fórmula 
de conversão é:  H = M ∗0,0001, sendo M a área em metros quadrados é H a área em hectares. ''' 

metro = float(input("Digite a área em metros quadradros: "))

hectares = metro * 0.0001

print(f"O valor da área {metro} em metros quadrados convertido em hectares é {hectares}")
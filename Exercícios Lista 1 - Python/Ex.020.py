''' 20. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A 
fórmula de conversão é P = C / 2.54, sendo C o comprimento em centímetros e P o comprimento 
em polegadas. ''' 

centimetro = float(input("Digite o valor em centímetros: "))

polegada = centimetro / 2.54

print(f"O valor em centímetro {centimetro} convertido em polegadas é {polegada:.2f}")
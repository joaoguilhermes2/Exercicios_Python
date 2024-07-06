''' 34. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um 
cilindro circular e calculado por meio da seguinte fórmula V = π ∗ raio2 ∗ altura, onde π = 
3.141592. ''' 

altura_cilindro = float(input("Digite a altura do cilindro: "))
raio_cilindro = float(input("Digite o raio do cilindro: "))

volume_cilindro = 3.141592 * (raio_cilindro * raio_cilindro) * altura_cilindro

print(f"O volume do cilindro é {volume_cilindro:.2f}")
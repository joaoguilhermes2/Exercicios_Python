''' 24. Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = (basemaior + basemenor) * altura / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero. '''

base_maior = float(input("Digite a base maior do trapézio: "))
base_menor = float(input("Digite a base menor do trapézio: "))
altura = float(input("Digite a altura do trapézio: "))

if base_maior > 0 and base_menor > 0:
    area_trapezio = ((base_maior + base_menor) * altura) / 2
    print(f"A área do trapézio é {area_trapezio}")
else:
    print("A base maior e a base menor são menores que 0!")
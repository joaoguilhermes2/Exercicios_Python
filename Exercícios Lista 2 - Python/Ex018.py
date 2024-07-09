''' 18. Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
utilizando as seguintes formulas (onde h corresponde à altura): 
• Homens: (72.7∗ h)−58 
• Mulheres: (62,1∗ h)−44,7 ''' 

altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo (M-masculino / F-feminino): ")

if sexo == 'M':
    peso_homem = (72.7 * altura) - 58
    print(f"O seu peso ideal é {peso_homem:.2f}")
elif sexo == 'F':
    peso_mulher = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {peso_mulher:.2f}")
else:
    print("Sexo Inválido!")
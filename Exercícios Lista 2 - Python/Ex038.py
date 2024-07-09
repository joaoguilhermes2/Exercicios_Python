''' 38. Crie um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a 
tabela abaixo: 
IMC          | Classificação
<18,5        |  Abaixo do peso
18,6 - 24,9  |  Saudável
25,0 - 29,9  |  Peso em Excesso
30,0 - 34,9  |  Obesidade Grau 1
35,0 - 39,9  |  Obesidade Grau 2 (severa)
>= 40,0      |  Obesidade Grau 3 (mórbida)
''' 

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do Peso")
elif 18.5 <= imc < 25.0:
    print("Saudável")
elif 25.0 <= imc < 30.0:
    print("Peso em excesso")
elif 30.0 <= imc < 35.0:
    print("Obesidade Grau I")
elif 35.0 <= imc < 40.0:
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (mórbida)")
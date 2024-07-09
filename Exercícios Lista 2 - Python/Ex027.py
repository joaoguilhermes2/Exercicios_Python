''' 27. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se 
forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos: 
• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados. 
• Chama-se equilátero o triângulo que tem três lados iguais. 
• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais. 
• Recebe o nome de escaleno o triângulo que tem os três lados diferentes. '''

a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero!")
    elif a == b or b == a or a == c or c == a:
        print("Triângulo Isósceles!")
    elif a != b != c or b != a != c or c != b != a:
        print("Triângulo Escaleno!")
    else:
        print("Valor Inválido!")
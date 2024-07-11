''' 26. Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3 
x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente 
(y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para 
resolver o problema utilize estrutura de repetição. ''' 

contador = 0
resultado = 1

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor do expoente y: "))

while contador < y:
    resultado *= x # Operador "*=" é usado para realizar a exponenciação!
    contador += 1

print(f"O resultado de {x}^{y} é: {resultado}")
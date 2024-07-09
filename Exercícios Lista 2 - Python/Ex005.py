''' 5. Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:  
F - Feminino, M – Masculino ou Sexo Inválido. ''' 

letra = input("Selecione a letra referente ao seu sexo (F-feminino/M-masculino): ")

if letra == 'F':
    print("Você é uma mulher!")
elif letra == 'M':
    print("Você é um homem!")
else:
    print("Sexo Inválido!")
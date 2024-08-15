while True:
    try:
        letra = input("Selecione a letra referente ao seu sexo (F-feminino/M-masculino): ")

        if letra == 'F':
            print("Você é uma mulher!")
        elif letra == 'M':
            print("Você é um homem!")
        else:
            print("Sexo Inválido!")
            
    except:
        print("Entrada Inválida, digite novamnente!")
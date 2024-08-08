''' Crie uma função que imprima a quantidade de dígitos de um 
determinado número inteiro informado. '''

try: # Tratamento de Exceção
    def contar_digitos(numero):
        if numero < 0:
            numero = -numero  # Torna o número positivo se for negativo: "-numero torna o o número positivo em negativo e vice versa"
        quantidade_digitos = len(str(numero))  # Converte o número para string e conta o comprimento
        print(f"A quantidade de dígitos no número é: {quantidade_digitos}")
except:
    print("Valor Inválido!")

contar_digitos(12345)
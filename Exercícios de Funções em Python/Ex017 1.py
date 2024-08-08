''' Crie uma função que armazene os dados de uma pessoa em um 
dicionário e imprima-os na tela. Utilize argumentos nomeados 
**kwargs. '''

def dados_pessoa(**kwargs):
    dados_pessoa = kwargs
    
    for chave, valor in dados_pessoa.items():
        print(f"{chave}: {valor}")

dados_pessoa(nome="João Guilherme", sobrenome="Ortigosa", email="joooa@hot.com",cidade="Campo Grande",idade="18 Anos",celular="+55(22) 123456789")
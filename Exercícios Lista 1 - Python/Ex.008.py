# 8. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual. 

idade = int(input("Digite a sua idade: "))
ano_atual = int(input("Digite o ano atual: "))

ano_nascimento = ano_atual - idade

print(f"Você nasceu em {ano_nascimento}")
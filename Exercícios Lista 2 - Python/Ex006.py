''' 6. Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V- 
Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
"Valor Inválido!", conforme o caso. '''

turno = input("Digite em qual turno você estuda (M-matutino / V-vespertino / N-noturno): ")

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
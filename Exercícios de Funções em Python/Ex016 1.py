''' Crie uma função que receba múltiplos argumentos não nomeados, 
considere que a função receba números flutuantes como argumentos 
e retorne a média dos argumentos. '''

def media(d,f,g,h):
    media = (d + f + g + h) / 4
    return media

res = media(5,6,7,10)
print(f"A media é: {res}")


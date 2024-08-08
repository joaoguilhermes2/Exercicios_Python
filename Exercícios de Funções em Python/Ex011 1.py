def imprimir_lista_numerada(lista):
    for i, item in enumerate(lista, start=1):
        print(f"{i}, {item}")

frutas = ['Pera', 'Uva', 'Maçã', 'Salada mista']
imprimir_lista_numerada(frutas)

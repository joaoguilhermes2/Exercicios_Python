class Livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self,nova_editora):
        self.editora = nova_editora
    
    def listar_quant_paginas(self):
        return self.paginas
    
livro1 = Livro(2010,"George Orwell","Companhia das Letras",328)
print("Editora Original:",livro1.editora)

livro1.alterar_editora("Editora Nova")
print("Editora após a alteração:",livro1.editora)

print("Número de páginas:",livro1.listar_quant_paginas())
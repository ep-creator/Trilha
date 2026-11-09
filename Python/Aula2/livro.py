class Livro():

    def __init__(self, titulo, autor, paginas, paginas_lidas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = paginas_lidas

    def ler(self, quantidade):
        self.paginas_lidas += quantidade
        if self.paginas_lidas > self.paginas:
            self.paginas_lidas = self.paginas

    def progresso(self):
        progresso = self.paginas_lidas / self.paginas
        print(f"{progresso * 100:.1f}% lido")

l1 = Livro("pequeno principe", "o autor", 1000, 500)

l1.progresso()
l1.ler(100)
l1.progresso()
l1.ler(1000)
l1.progresso()


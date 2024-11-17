class Media:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def play(self):
        raise NotImplementedError("Subclasses should implement this method")
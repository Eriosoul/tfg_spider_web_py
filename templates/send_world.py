class SendWorld:
    def __init__(self):
        self.world: str = ""

    def get_world(self):
        self.world: str = input("Introduce el producto que deseas buscar: ")
        palabra = self.world
        return palabra

    def obtener_palabra(self, palabra):
        return palabra
class SendWorld:
    def __init__(self):
        self.world: str = ""

    def get_world(self):
        self.world: str = input("Introduce el producto que deseas buscar: ")
        search_word = self.world
        return search_word

    def obtener_palabra(self, search_word):
        return search_word
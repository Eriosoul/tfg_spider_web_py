class SendWorld:
    def __init__(self):
        self.world: str = ""

    def get_world(self):
        self.world: str = input("Introduce el producto que deseas buscar: ")
        return self.world
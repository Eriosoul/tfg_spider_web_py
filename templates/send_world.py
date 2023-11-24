class SendWorld:
    def __init__(self):
        self.world: str = ""

    def get_world(self):
        # se solicita la palabra solo una vez y se guarda, despues procede a utilizar dicha palabra
        while True: # hacemos un bucle while true para que hata no s eintroduzca la palabra que no empiece el scraping

            self.world = input("Introduce el producto que deseas buscar: ")
            try:
                # comprobamos si hay palabra y si no son solo numeros
                if not self.world or self.world.isdigit():
                    # nostramos el error para que vuelva a intoducir lo que quiere buscar
                    print("Debe introducir el producto que desea buscar.")
                else:
                    return self.world
            except Exception as e:
                print("Error: ", e)
                return None

    # def obtener_palabra(self, search_word):
    #     return search_word
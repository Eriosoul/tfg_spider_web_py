import os
class GetPathJson:
    def __init__(self):
        self.get_path_consum = ""
        self.get_path_carrefour = ""

    def driver_path(self):
        try:
            print("Obteniendo rutas del json: ")
            current_directory = os.path.dirname(os.path.realpath(__file__))
            self.get_path_consum = os.path.join(current_directory, "consum.json")
            self.get_path_carrefour = os.path.join(current_directory, "carrefour.json")
            return self.get_path_consum, self.get_path_carrefour
        except Exception as e:
            print("Error:", e)
            return None
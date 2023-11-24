import os
class GetPathDriver:
    def __init__(self):
        self.get_path_driver = ""

    def driver_path(self):
        try:
            # estaba teniendo problemas cuando intentaba pasar una ruta no absoluta
            # busque otra froma para obtener la ruta del driver para que no de problemas
            current_directory = os.path.dirname(os.path.realpath(__file__))
            self.get_path_driver = os.path.join(current_directory, "chromedriver.exe")
            return self.get_path_driver
        except Exception as e:
            print("Error:", e)
            return None
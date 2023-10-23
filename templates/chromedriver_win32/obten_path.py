import os
class GetPathDriver:
    def __init__(self):
        self.get_path_driver = ""

    def driver_path(self):
        try:
            current_directory = os.path.dirname(os.path.realpath(__file__))
            self.get_path_driver = os.path.join(current_directory, "chromedriver.exe")
            return self.get_path_driver
        except Exception as e:
            print("Error:", e)
            return None
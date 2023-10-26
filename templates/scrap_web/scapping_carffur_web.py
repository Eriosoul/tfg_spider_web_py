import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from templates.chromedriver_win32.obten_path import GetPathDriver


class CarrefourWeb:
    def __init__(self, palabra):
        # Configurar opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        # Obtén la ruta al directorio actual
        # self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.chrom_driver_path = GetPathDriver()
        # Obtener la palabra
        self.word = palabra
        self.data = []

    def cheking_driver(self):
        try:
            print(f"La ruta es: {self.chrom_driver_path.driver_path()}")
            # Construye la ruta al ejecutable de ChromeDriver
            # chrome_path = r'E:\Deusto_Python\tfg_spider_web_py\templates\chromedriver_win32\chromedriver.exe'
            chrome_path = self.chrom_driver_path.driver_path()
            return chrome_path
        except Exception as e:
            print("Error al comprobar los drivers: ",e)


    @staticmethod
    def navigate_to_carrefour(driver):
        print("Comprobando estado cons ervidor de carrefour...")
        try:
            url = 'https://www.carrefour.es/'
            driver.get(url)
            time.sleep(5)
        except Exception as e:
            print("Error con el servidor de carreforur:", e)
            raise e

    def check_word(self):
        word = self.word.replace(" ", "+")
        return word

    def get_new_link(self, driver):
        print("Creando nuevo link de busqueda... ")
        try:
            link2 = 'https://www.carrefour.es/?q='
            url_search = link2 + self.check_word()
            print(url_search)
            driver.get(url_search)
            time.sleep(5)
        except Exception as e:
            print("Error con la nueva URL:", e)
            raise e

    @staticmethod
    def get_page_content(driver):
        # Obtener el contenido de la página después de cargar el contenido dinámico
        page_content = driver.page_source
        time.sleep(3)
        return page_content

    @staticmethod
    def extract_product_info(page_content):
        soup = BeautifulSoup(page_content, 'html.parser')

        product_info = []
        brand_spans = soup.find_all("strong", class_="ebx-result-price__value")
        info = soup.find_all("h1", class_="ebx-result-title ebx-result__title")
        precio_kg_l = soup.find_all("div", class_="ebx-result__quantity ebx-result-quantity")
        for brand, info_product, precio_l in zip(brand_spans, info, precio_kg_l):
            product_info.append({
                "Nombre": info_product.text,
                "Precio": brand.text,
                "Precio_KG/L": precio_l.text
            })
        time.sleep(1)
        return product_info

    def next_step(self, chrome_path):
        with webdriver.Chrome(service=ChromeService(chrome_path), options=self.chrome_options) as driver:
            self.navigate_to_carrefour(driver)
            self.get_new_link(driver)
            page_content = driver.page_source

            product_info = self.extract_product_info(page_content)

            for item in product_info:
                print("Nombre", item["Nombre"])
                print("Precio: ", item["Precio"])
                print("Precio KG/L: ", item["Precio_KG/L"])
                print("--------------------")
            self.data.extend(product_info)
            time.sleep(5)

    def save_data_to_json(self, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)

def main_carrefour(palabra):
    try:
        c = CarrefourWeb(palabra)
        data = c.cheking_driver()
        c.next_step(data)
        c.save_data_to_json('carrefour.json')
    except Exception as e:
        print("Error:", e)

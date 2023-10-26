import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# from templates.send_world import SendWorld
from templates.chromedriver_win32.obten_path import GetPathDriver


class ConsumWeb:
    def __init__(self, palabra):
        # Configurar opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        # Obtén la ruta al directorio actual
        # self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.chrom_driver_path = GetPathDriver()

        # self.word = SendWorld()
        # palabra_obtenida = self.word.obtener_palabra(self.word)
        # print("Palabra obtenida:", palabra_obtenida)
        self.palabra = palabra
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
    def navigate_to_consum_web(driver):
        # Navegar a la URL de Consum
        print("Comprobando estado con servidor...")
        try:
            url = 'https://tienda.consum.es/es/'
            driver.get(url)
            time.sleep(5)
        except Exception as e:
            print("Error con Consum URL:", e)
            raise e
    def check_word(self):
        word = self.palabra.replace(" ", "%20")  # Reemplazar espacios en blanco con '%20'
        return word
    def navigate_to_cervezas(self, driver):
        # Navegar a la página de de la busqueda
        print("Creando nuevo link de busqueda... ")
        try:
            link2 = 'https://tienda.consum.es/es/s/'
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
        return page_content

    @staticmethod
    def extract_product_info(page_content):
        # Parse the HTML content
        soup = BeautifulSoup(page_content, 'html.parser')

        # Extract product names and prices
        product_info = []
        brand_spans = soup.find_all("span", id="grid-widget--brand")
        info_name = soup.find_all("a", id="grid-widget--descr")
        price_L = soup.find_all("p", id="grid-widget--unitprice")
        price_spans = soup.find_all("span", id="grid-widget--price")

        for brand, info, price_litre ,price in zip(brand_spans, info_name, price_L,price_spans):
            product_info.append({
                "Nombre": brand.text,
                "Informacion": info.text,
                "Precio_l_kg": price_litre.text,
                "Precio": price.text
            })
        time.sleep(1)
        return product_info

    def next_step(self, chrome_path):
        with webdriver.Chrome(service=ChromeService(chrome_path), options=self.chrome_options) as driver:
            self.navigate_to_consum_web(driver)
            self.navigate_to_cervezas(driver)
            page_content = driver.page_source

            product_info = self.extract_product_info(page_content)

            for item in product_info:
                print("Nombre:", item["Nombre"])
                print("Informacion adiciona:", item["Informacion"])
                print("Precio L/KG:", item["Precio_l_kg"])
                print("Precio:", item["Precio"])
                print("--------------------")
            self.data.extend(product_info)
            time.sleep(5)

    def save_data_to_json(self, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)
def main_consum(palabra):
    try:
        c = ConsumWeb(palabra)
        data = c.cheking_driver()
        c.next_step(data)
        c.save_data_to_json('consum.json')
    except Exception as e:
        print("Error:", e)


    # @staticmethod
    # def print_cervezas_info(brand_spans, price_spans):
    #     # Iterar sobre las cervezas y mostrar el nombre y el precio
    #     for brand, price in zip(brand_spans, price_spans):
    #         print("Nombre:", brand.text)
    #         print("Precio:", price.text)
    #         print("--------------------")
    #
    # def next_step(self, chrome_path):
    #     # Initialize the Selenium driver
    #     with webdriver.Chrome(service=ChromeService(chrome_path), options=self.chrome_options) as driver:
    #         self.navigate_to_consum_web(driver)
    #         self.navigate_to_cervezas(driver)
    #         page_content = self.get_page_content(driver)
    #
    #         # Print the content of the page
    #         print(f"\nContenido de la página de {self.word}:")
    #         # print(page_content)  # Comment out to avoid printing the entire page
    #
    #         # Get the name and price of each cerveza
    #         brand_spans = driver.find_elements("css selector", "span#grid-widget--brand")
    #         price_spans = driver.find_elements("css selector", "span#grid-widget--price")
    #
    #         self.print_cervezas_info(brand_spans, price_spans)
    #         time.sleep(5)
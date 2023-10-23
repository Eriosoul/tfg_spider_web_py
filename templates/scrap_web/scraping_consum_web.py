# import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from templates.send_world import SendWorld
from templates.chromedriver_win32.obten_path import GetPathDriver


class ConsumWeb:
    def __init__(self):
        # Configurar opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        # Obtén la ruta al directorio actual
        # self.current_directory = os.path.dirname(os.path.realpath(__file__))
        self.chrom_driver_path = GetPathDriver()
        # Obtener la palabra
        self.word = SendWorld()

    def cheking_driver(self):
        try:
            print(f"La ruta es: {self.chrom_driver_path.driver_path()}")
            # Construye la ruta al ejecutable de ChromeDriver
            # chrome_path = r'E:\Deusto_Python\tfg_spider_web_py\templates\chromedriver_win32\chromedriver.exe'
            chrome_path = self.chrom_driver_path.driver_path()
            return chrome_path
        except Exception as e:
            print(e)

    @staticmethod
    def navigate_to_consum_web(driver):
        # Navegar a la URL de Consum
        url = 'https://tienda.consum.es/es/'
        driver.get(url)
        time.sleep(5)

    def navigate_to_cervezas(self, driver):
        # Navegar a la página de cervezas
        link2 = 'https://tienda.consum.es/es/s/'
        url_cervezas = link2 + self.word.get_world()
        driver.get(url_cervezas)
        time.sleep(5)

    @staticmethod
    def get_page_content(driver):
        # Obtener el contenido de la página después de cargar el contenido dinámico
        page_content = driver.page_source
        return page_content

    @staticmethod
    def print_cervezas_info(brand_spans, price_spans):
        # Iterar sobre las cervezas y mostrar el nombre y el precio
        for brand, price in zip(brand_spans, price_spans):
            print("Nombre:", brand.text)
            print("Precio:", price.text)
            print("--------------------")

    def next_step(self, chrome_path):
        # Initialize the Selenium driver
        with webdriver.Chrome(service=ChromeService(chrome_path), options=self.chrome_options) as driver:
            self.navigate_to_consum_web(driver)
            self.navigate_to_cervezas(driver)
            page_content = self.get_page_content(driver)

            # Print the content of the page
            print(f"\nContenido de la página de {self.word}:")
            # print(page_content)  # Comment out to avoid printing the entire page

            # Get the name and price of each cerveza
            brand_spans = driver.find_elements("css selector", "span#grid-widget--brand")
            price_spans = driver.find_elements("css selector", "span#grid-widget--price")

            self.print_cervezas_info(brand_spans, price_spans)
            time.sleep(5)

def main():
    try:
        c = ConsumWeb()
        data = c.cheking_driver()
        c.next_step(data)
    except Exception as e:
        print("Error:", e)

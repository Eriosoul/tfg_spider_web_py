import os
import json
import time
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from templates.chromedriver_win32.obten_path import GetPathDriver


class CarrefourWeb:
    def __init__(self, search_word):
        load_dotenv()
        # Configurar opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        # obtenemos la ruta del driver
        self.chrom_driver_path = GetPathDriver()
        # Obtener la palabra
        self.link_check = os.getenv("FIRST_LINK_CHECK")
        self.generate_link = os.getenv("FIRST_LINK")
        self.word = search_word
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


    def navigate_to_carrefour(self,driver):
        print("Comprobando estado cons ervidor de carrefour...")
        try:
            # comprobacion con la web oficial para saber si no esta caida
            url = self.link_check
            driver.get(url)
            time.sleep(5)
        except Exception as e:
            print("Error con el servidor de carreforur:", e)
            raise e

    def check_word(self):
        # Reemplazar espacios en blanco con '+' ej: "chocolate+milka"
        word = self.word.replace(" ", "+")
        return word

    def get_new_link(self, driver):
        print("Creando nuevo link de busqueda... ")
        try:
            # se crea el nuevo link con la palabra ya modificada "chocolate+milka"
            link2 = self.generate_link
            url_search = link2 + self.check_word()
            print(url_search)
            driver.get(url_search)
            time.sleep(5)
        except Exception as e:
            print("Error con la nueva URL:", e)
            raise e

    @staticmethod
    def get_page_content(driver):
        # Obtener el contenido de la pagina despues de cargar el contenido dinamico
        page_content = driver.page_source
        time.sleep(3)
        return page_content

    @staticmethod
    def extract_product_info(page_content):
        # procedemos a realizar el scrap de contenido de la pagina web
        soup = BeautifulSoup(page_content, 'html.parser')
        # guardamos la informacion en poduct_info=[]
        product_info = []
        # obtenemos directamente el nombre, informacion, precio etc
        brand_spans = soup.find_all("strong", class_="ebx-result-price__value")
        info = soup.find_all("h1", class_="ebx-result-title ebx-result__title")
        precio_kg_l = soup.find_all("div", class_="ebx-result__quantity ebx-result-quantity")
        for brand, info_product, precio_l in zip(brand_spans, info, precio_kg_l):
            product_info.append({
                # los añadimos a la lista, ya que debe de haber varios
                "Nombre": info_product.text,
                "Precio": brand.text,
                "Precio_KG/L": precio_l.text
            })
        time.sleep(1)
        return product_info

    def next_step(self, chrome_path):
        # se procede a usar el driver cuando se inicia la busuqueda
        with webdriver.Chrome(service=ChromeService(chrome_path), options=self.chrome_options) as driver:
            # se llama a la funciones
            self.navigate_to_carrefour(driver)
            self.get_new_link(driver)
            page_content = driver.page_source
            # guardamos los poductos extraidos de la funcion anterior
            product_info = self.extract_product_info(page_content)
            # muestro los productos
            for item in product_info:
                print("Nombre", item["Nombre"])
                print("Precio: ", item["Precio"])
                print("Precio KG/L: ", item["Precio_KG/L"])
                print("--------------------")
            self.data.extend(product_info)
            time.sleep(5)

    def save_data_to_json(self, file_path):
        # leemos el json y guardamos los poductos en dicho json
        with open(file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)

def main_carrefour(search_word):
    try:
        c = CarrefourWeb(search_word)
        data = c.cheking_driver()
        c.next_step(data)
        c.save_data_to_json('carrefour.json')
    except Exception as e:
        print("Error:", e)

import os
import json
import time
# from tqdm import tqdm
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from templates.chromedriver_win32.obten_path import GetPathDriver


class ConsumWeb:
    def __init__(self, search_word):
        load_dotenv()
        # Configurar opciones de Chrome
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        self.chrom_driver_path = GetPathDriver()
        self.second_link_check = os.getenv("SECOND_LINK_CHECK")
        self.generate_second_link = os.getenv("SECOND_LINK")
        self.word = search_word
        self.data = []
    def cheking_driver(self):
        try:
            print(f"La ruta es: {self.chrom_driver_path.driver_path()}")
            chrome_path = self.chrom_driver_path.driver_path()
            return chrome_path
        except Exception as e:
            print("Error al comprobar los drivers: ",e)


    def navigate_to_consum_web(self, driver):
        print("Comprobando estado con servidor...")
        try:
            url = self.second_link_check
            driver.get(url)
            time.sleep(5)
        except Exception as e:
            print("Error con Consum URL:", e)
            raise e
    def check_word(self):
        word = self.word.replace(" ", "%20")
        return word
    def navigate_to_cervezas(self, driver):
        print("Creando nuevo link de busqueda... ")
        try:
            link2 = self.generate_second_link
            url_search = link2 + self.check_word()
            print(url_search)
            driver.get(url_search)
            time.sleep(5)
        except Exception as e:
            print("Error con la nueva URL:", e)
            raise e

    @staticmethod
    def get_page_content(driver):
        page_content = driver.page_source
        return page_content

    @staticmethod
    def extract_product_info(page_content):
        soup = BeautifulSoup(page_content, 'html.parser')

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
        # leemos el json y guardamos los poductos en dicho json
        with open(file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)
def main_consum(search_word):
    try:
        c = ConsumWeb(search_word)
        data = c.cheking_driver()
        c.next_step(data)
        c.save_data_to_json('consum.json')
    except Exception as e:
        print("Error:", e)

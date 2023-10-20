import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from templates.send_world import SendWorld
# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Obtén la ruta al directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construye la ruta al ejecutable de ChromeDriver
chrome_path = r'E:\Deusto_Python\tfg_spider_web_py\templates\chromedriver_win32\chromedriver.exe'
palabra = SendWorld()
# Inicializar el driver de Selenium
with webdriver.Chrome(service=ChromeService(chrome_path), options=chrome_options) as driver:
    # Navegar a la URL
    url = 'https://tienda.consum.es/es/'
    driver.get(url)

    # Esperar un momento para asegurar que la página se cargue completamente
    time.sleep(5)

    # Navegar a la página de cervezas
    link2 = 'https://tienda.consum.es/es/s/'
    url_cervezas = link2 + palabra.get_world()
    driver.get(url_cervezas)

    # Esperar un momento para que la página de cervezas se cargue completamente
    time.sleep(5)

    # Obtener el contenido de la página después de cargar el contenido dinámico
    page_content = driver.page_source

    # Imprimir el contenido de la página
    print("Contenido de la página de cervezas:")
    # print(page_content)  # Comentar para no imprimir toda la página

    # Obtener el nombre y el precio de cada cerveza
    brand_spans = driver.find_elements("css selector", "span#grid-widget--brand")
    price_spans = driver.find_elements("css selector", "span#grid-widget--price")

    # Iterar sobre las cervezas y mostrar el nombre y el precio
    for brand, price in zip(brand_spans, price_spans):
        print("Nombre:", brand.text)
        print("Precio:", price.text)
        print("--------------------")

    time.sleep(5)

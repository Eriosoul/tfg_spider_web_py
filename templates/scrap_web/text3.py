# import os
# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# # from bs4 import BeautifulSoup
#
# # Configurar opciones de Chrome
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
#
# # Encabezados personalizados
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
# }
#
# # Obtén la ruta al directorio actual
# current_directory = os.path.dirname(os.path.realpath(__file__))
#
# # Construye la ruta al ejecutable de ChromeDriver
# chrome_path = r'E:\Deusto_Python\tfg_spider_web_py\templates\chromedriver_win32\chromedriver.exe'
# print(chrome_path)
#
# # Inicializar el driver de Selenium
# with webdriver.Chrome(service=ChromeService(chrome_path), options=chrome_options) as driver:
#     # Configurar los headers en la solicitud
#     for key, value in headers.items():
#         chrome_options.add_argument(f'--{key}={value}')
#
#     # Navegar a la URL
#     url = 'https://tienda.consum.es/es/'
#     driver.get(url)
#
#     # Obtener las cookies después de cargar la página
#     cookies = driver.get_cookies()
#
#     # Imprimir las cookies
#     print("Cookies:")
#     for cookie in cookies:
#         print(f"{cookie['name']}: {cookie['value']}")
#
#     driver.implicitly_wait(10)
#
#     page_content = driver.page_source
#     print(page_content)
#     time.sleep(5)
#     # Realizar la solicitud con las cookies y los encabezados
#     url2= "https://tienda.consum.es/es/s/cerveza?orderById=13&page=1"
#     cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
#     response = requests.get(url2, cookies=cookies_dict, headers=headers)
#     time.sleep(1)
#     # Verificar si la solicitud fue exitosa (código de estado 200)
#     if response.status_code == 200:
#         print("Solicitud exitosa!")
#         print("Contenido de la página:")
#         print(response.text)
#     else:
#         print("La solicitud no fue exitosa. Código de estado:", response.status_code)
#     # Analizar el contenido con BeautifulSoup
#     # soup = BeautifulSoup(page_content, 'html.parser')
#     # print(soup.contents)
#     # print("-------------------------")
#     # print(soup.text)
#     # print(driver.title)
#     # search = driver.find_element_by_name("s")
#     # search.send_keys("cerveza")
#     # search.send_keys(Keys.RETURN)
#     # time.sleep(5)

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Obtén la ruta al directorio actual
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construye la ruta al ejecutable de ChromeDriver
chrome_path = r'E:\Deusto_Python\tfg_spider_web_py\templates\chromedriver_win32\chromedriver.exe'

# Inicializar el driver de Selenium
with webdriver.Chrome(service=ChromeService(chrome_path), options=chrome_options) as driver:
    # Navegar a la URL
    url = 'https://tienda.consum.es/es/'
    driver.get(url)

    # Esperar un momento para asegurar que la página se cargue completamente
    time.sleep(5)

    # Navegar a la página de cervezas
    url_cervezas = 'https://tienda.consum.es/es/s/cerveza?orderById=13&page=1'
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

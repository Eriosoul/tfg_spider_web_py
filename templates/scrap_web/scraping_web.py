import time
# from difflib import SequenceMatcher

import requests
from requests import Response
from bs4 import BeautifulSoup
from templates.send_world import SendWorld

class ScrapWeb:
    def __init__(self):
        self.url = 'https://tienda.consum.es/es/s/'
        self.before = '?orderById=13&page=1'
        self.main_instance = SendWorld()
    def check_status(self):
        time.sleep(1)
        try:
            r: Response = requests.get(self.url)
            if r.status_code == 200:
                # word = input("Introduzca la palabra que desea buscar: ")
                word = self.main_instance.get_world()
                modified_word = word.replace(' ', '%20')
                print(modified_word)
                return modified_word
            else:
                print(r.status_code)
                return None
        except Exception as e:
            print("Error con el servidor", e)
            return None

    def generate_link(self, modified_word):
        time.sleep(1)
        try:
            link = self.url + modified_word + self.before
            print(link)
            r: Response = requests.get(link)
            if r.status_code == 200:
                print("Obteniendo datos")
                soup = BeautifulSoup(r.content, "html.parser")
                print(soup.contents)
                print("Pruebas")
                html = r.text
                print(html)
                print("=========================\n", r.json())
            else:
                print("Error con el servidor" ,r.status_code)
            return link
        except Exception as e:
            print(e)
            return None

def main_scrap():
    time.sleep(1)
    s: ScrapWeb = ScrapWeb()
    add_word = s.check_status()
    s.generate_link(add_word)

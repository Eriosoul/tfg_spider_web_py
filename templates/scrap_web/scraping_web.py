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
            else:
                print("Error con el servidor" ,r.status_code)
            return link
        except Exception as e:
            print(e)
            return None

    # def similar(self, a, b):
    #     return SequenceMatcher(None, a, b).ratio()
    # def get_scrap_web(self, link):
    #     try:
    #         info = self.generate_link(link)
    #         soup = BeautifulSoup("html.parser", info.text)
    #         print(soup)
    #     except Exception as e:
    #         print(e)

def main_scrap():
    time.sleep(1)
    s: ScrapWeb = ScrapWeb()
    add_word = s.check_status()
    s.generate_link(add_word)

# if __name__ == '__main__':
#     time.sleep(1)
#     s: ScrapWeb = ScrapWeb()
#     add_word = s.check_status()
#     s.generate_link(add_word)
#     similarity_ratio = s.similar("hello", "hella")
#     print("Similarity ratio:", similarity_ratio)

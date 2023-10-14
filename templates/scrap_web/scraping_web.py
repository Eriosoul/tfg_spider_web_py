import requests
from requests import Response

class ScrapWeb:
    def __init__(self):
        self.url = 'https://www.carrefour.es'
        self.after = '/?q='
        self.before = '%20'

    def check_status(self):
        try:
            r: Response = requests.get(self.url)
            if r.status_code == 200:
                word = input("Introduzca la palabra que desea buscar: ")
                modified_word = word.replace(' ', '+')
                print(modified_word)
                return modified_word
            else:
                print(r.status_code)
                return None
        except Exception as e:
            print("Error con el servidor", e)
            return None

    def generate_link(self, modified_word):
        try:
            link = self.url + self.after + modified_word + self.before
            print(link)
            r: Response = requests.get(link)
            if r.status_code == 200:
                print("Obteniendo datos")
            else:
                print("Error con el servidor" ,r.status_code)
            return link
        except Exception as e:
            print(e)
            return None


if __name__ == '__main__':
    s: ScrapWeb = ScrapWeb()
    add_word = s.check_status()
    s.generate_link(add_word)

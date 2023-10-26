from templates.send_world import SendWorld
from templates.scrap_web import scraping_consum_web
from templates.scrap_web import scapping_carffur_web
from templates.comprobate.checking_priece import main_comparation

def main():
    palabra = SendWorld().get_world()
    print("Obteniendo información de consum")
    scraping_consum_web.main_consum(palabra)
    print("Obteniendo información de carrefour")
    scapping_carffur_web.main_carrefour(palabra)
    main_comparation()

if __name__ == '__main__':
    main()

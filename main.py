from templates.send_world import SendWorld
from templates.scrap_web import scraping_consum_web
from templates.scrap_web import scapping_carffur_web
from templates.comprobate.checking_priece import main_comparation

def main():
    # hace llamada a la obtencion de palabra
    search_word = SendWorld().get_world()
    print("Obteniendo información de consum")
    # se pasa la palabra para realizar la busqueda
    scraping_consum_web.main_consum(search_word)
    print("Obteniendo información de carrefour")
    scapping_carffur_web.main_carrefour(search_word)
    main_comparation()

# se llama al main
if __name__ == '__main__':
    main()

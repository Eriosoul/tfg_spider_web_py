import time
from tqdm import tqdm
from templates.send_world import SendWorld
from templates.scrap_web import scraping_consum_web
from templates.scrap_web import scapping_carffur_web
from templates.comprobate.checking_priece import main_comparation

def main():
    # hace llamada a la obtencion de palabra
    search_word = SendWorld().get_world()
    print("Obteniendo información de consum")
    for _ in tqdm(range(10), desc="Progreso Consum", unit="iter"):
        # Simula la ejecución de la función (reemplaza esto con tu lógica real)
        time.sleep(0.1)
    scraping_consum_web.main_consum(search_word)
    print("Obteniendo información de carrefour")
    for _ in tqdm(range(10), desc="Progreso Carrefour", unit="iter"):
        # Simula la ejecución de la función (reemplaza esto con tu lógica real)
        time.sleep(0.1)
    scapping_carffur_web.main_carrefour(search_word)
    print("Obteniendo información de comparación")
    for _ in tqdm(range(10), desc="Progreso Comparación", unit="iter"):
        # Simula la ejecución de la función (reemplaza esto con tu lógica real)
        time.sleep(0.1)
    main_comparation()

# se llama al main
if __name__ == '__main__':
    main()

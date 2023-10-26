import json
from difflib import SequenceMatcher
from get_json_data import GetPathJson


class DiferenceByProduct:
    def __init__(self):
        # self.consum = 'Deusto_Python/tfg_spider_web_py/consum.json'
        self.get_json_paths = GetPathJson()  # Crea una instancia de GetPathJson
        self.consum, self.carrefour = self.get_json_paths.driver_path()
        print(self.consum)
        print(self.carrefour)

    def data_json_consum(self):
        print("Comrpobando datos recopilado de Carrefour...")
        try:
            with open(self.consum) as file:
                data_consum = json.load(file)
                return data_consum
        except FileNotFoundError:
            return []

    def data_json_carrefour(self):
        print("Comrpobando datos recopilado de Carrefour...")
        try:
            with open(self.carrefour) as file:
                data_carrefour = json.load(file)
                return data_carrefour
        except FileNotFoundError:
            return []
    def similar(self, data_consum, data_carrefour):
        similarities = []

        for consum_product in data_consum:
            for carrefour_product in data_carrefour:
                similarity = SequenceMatcher(None, consum_product["Informacion"], carrefour_product["Nombre"]).ratio()
                similarities.append((consum_product, carrefour_product, similarity))

        similarities.sort(key=lambda x: x[2], reverse=True)

        return similarities


def main_comparation():
    d = DiferenceByProduct()
    data_consum = d.data_json_consum()
    data_carrefour = d.data_json_carrefour()

    similarities = d.similar(data_consum, data_carrefour)
    print("Mostrando todos los productos: ")
    for consum_product, carrefour_product, similarity in similarities:
        print(f'Similarity: {similarity:.2f}')
        print(f'Consum Product: {consum_product["Informacion"]} - {consum_product["Precio"]}')
        print(f'Carrefour Product: {carrefour_product["Nombre"]} - {carrefour_product["Precio"]}')
        print("--------------------")

    print("Mayor similitud: ")
    # Ordena las similitudes por similitud en orden descendente.
    similarities.sort(key=lambda x: x[2], reverse=True)

    # Imprime los 4 pares con la mayor similitud.
    for i, (consum_product, carrefour_product, similarity) in enumerate(similarities[:4]):
        print(f'Similarity {i + 1}: {similarity:.2f}')
        print(f'Consum Product: {consum_product["Informacion"]} - {consum_product["Precio"]}')
        print(f'Carrefour Product: {carrefour_product["Nombre"]} - {carrefour_product["Precio"]}')
        print("--------------------")

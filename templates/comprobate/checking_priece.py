import json
from difflib import SequenceMatcher


class DiferenceByProduct:
    def __init__(self):
        self.consum = 'E:/Deusto_Python/tfg_spider_web_py/consum.json'
        self.carrefour = 'E:/Deusto_Python/tfg_spider_web_py/carrefour.json'

    def data_json_consum(self):
        with open(self.consum) as file:
            data_consum = json.load(file)
            if data_consum is not None:
                print("Data exists!")
                return data_consum
            else:
                print("Data does not exist.")
                return []

    def data_json_carrefour(self):
        with open(self.carrefour) as file:
            data_carrefour = json.load(file)
            if data_carrefour is not None:
                print("Data exists!")
                return data_carrefour
            else:
                print("Data does not exist.")
                return []

    def similar(self, data_consum, data_carrefour):
        similarities = []

        for consum_product in data_consum:
            for carrefour_product in data_carrefour:
                similarity = SequenceMatcher(None, consum_product["Informacion"], carrefour_product["Nombre"]).ratio()
                similarities.append((consum_product, carrefour_product, similarity))

        similarities.sort(key=lambda x: x[2], reverse=True)

        return similarities


if __name__ == '__main__':
    d = DiferenceByProduct()
    data_consum = d.data_json_consum()
    data_carrefour = d.data_json_carrefour()

    similarities = d.similar(data_consum, data_carrefour)

    for consum_product, carrefour_product, similarity in similarities:
        print(f'Similarity: {similarity:.2f}')
        print(f'Consum Product: {consum_product["Informacion"]} - {consum_product["Precio"]}')
        print(f'Carrefour Product: {carrefour_product["Nombre"]} - {carrefour_product["Precio"]}')
        print("--------------------")

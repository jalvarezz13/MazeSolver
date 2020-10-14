import os
import json

class GestionJson:
    def __init__(self, rows, cols):
        data = {}
        self.rows = rows
        self.cols = cols
        data["rows"] = self.rows
        data["cols"] = self.cols
        data["max_n"] = 4,
        data["mov"] = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        data["id_mov"] = ["N", "E", "S", "O"]
        data["cells"] = self.crear_celdas()
        file_name = "Laberinto_wilson_B02_{0}x{1}.json".format(self.rows, self.cols)

        with open(os.path.join("{0}/JSONs".format(os.getcwd()), file_name), 'w') as file:
            json.dump(data, file)
        
        self.data = data

    def get_data(self):
        return self.data

    def crear_celdas(self):
        dic_cell = {}
        dic_data_cell = {}
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                dic_data_cell["value"] = 0
                dic_data_cell["neighbors"] = [False, False, False, False]
                dic_cell["({0}, {1})".format(i, j)] = dic_data_cell
        return dic_cell
        
    def leer_json(file_name):
        f = open("JSONs/{0}".format(file_name), "r")
        content = f.read()
        diccionario = json.loads(content)

        return diccionario

    def escribir_json(file_name, diccionario):
        with open("JSONs/{0}".format(file_name), 'r+') as f:
            f.seek(0)
            f.write(json.dumps(diccionario))
            f.truncate()
        
    def cambiar_vecinos(camino, lista_movimientos, diccionario):
        movimiento = diccionario["mov"]
        posicion_vecino = None
        file_name = "Laberinto_wilson_B02_{0}x{1}.json".format(diccionario["rows"], diccionario["cols"])

        diccionario = GestionJson.leer_json(file_name)

        for i in range(0, (len(camino) - 1)):
            if lista_movimientos[i] == movimiento[0]:
                posicion_vecino = 0
            elif lista_movimientos[i] == movimiento[1]:
                posicion_vecino = 1
            elif lista_movimientos[i] == movimiento[2]:
                posicion_vecino = 2
            elif lista_movimientos[i] == movimiento[3]:
                posicion_vecino = 3

            diccionario["cells"][str(camino[i])]["neighbors"][posicion_vecino] = True
            diccionario["cells"][str(camino[i + 1])]["neighbors"][(posicion_vecino + 2) % 4] = True

        GestionJson.escribir_json(file_name, diccionario)

        diccionario =  GestionJson.leer_json(file_name)

        return diccionario

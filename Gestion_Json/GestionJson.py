import os
import json
import sys

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
        file_name = "Laberinto_Wilson_B1_2_{0}x{1}.json".format(self.rows, self.cols)

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
        
    def leer_json(file_name): # REVISAR
        try:
            f = open(file_name, "r")
        except FileNotFoundError:
            file_name = "JSONs/" + file_name
            f = open(file_name, "r")
            content = f.read()
            diccionario = json.loads(content)
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
        file_name = "Laberinto_Wilson_B1_2_{0}x{1}.json".format(diccionario["rows"], diccionario["cols"])

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

    def check_json(diccionario):
        token = True
        for n in range(0, diccionario["cols"]):            
            if(diccionario["cells"]["(0, {0})".format(n)]["neighbors"][0] == True or 
            diccionario["cells"]["({0}, {1})".format(diccionario["rows"]-1, n)]["neighbors"][2] == True):
                token = False  
        
        for n in range(0, diccionario["rows"]):            
            if( diccionario["cells"]["({0}, 0)".format(n)]["neighbors"][3] == True or 
            diccionario["cells"]["({0}, {1})".format(n, diccionario["cols"]-1)]["neighbors"][1] == True):
                token = False           

        for i in range(0, diccionario["rows"]):
            for j in range(0, diccionario["cols"]):
                celdaAux1 = diccionario["cells"]["({0}, {1})".format(i, j)]
                for z in range(0, len(diccionario["mov"])):
                    coordFila = i + diccionario["mov"][z][0]
                    coordCol = j + diccionario["mov"][z][1]
                    try:
                        celdaAux2 = diccionario["cells"]["({0}, {1})".format(coordFila, coordCol)]
                        if (celdaAux1["neighbors"][z] != celdaAux2["neighbors"][(z+2)%4]):
                            print("Inconsistencia en la pared de la celda({0}, {1}) con la celda({2},{3})".format(i, j, coordFila, coordCol))
                            token = False
                    except KeyError:
                        pass

        if(token == False):                       
            sys.exit()        
        else:             
            print("JSON CORRECTED")
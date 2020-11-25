import json
import Cnfg

class LeerProblemaJson:
    def getData(file_name):

        f = open(file_name, "r")
        content = f.read()
        diccionario = json.loads(content)

        celda_inicio = diccionario["INITIAL"]
        celda_objetivo = diccionario["OBJETIVE"]
        maze = diccionario["MAZE"]

        Cnfg.inicial = (int(celda_inicio[1:celda_inicio.find(",")]), int(celda_inicio[celda_inicio.find(",")+2:len(celda_inicio)-1]))
        Cnfg.objetivo = (int(celda_objetivo[1:celda_objetivo.find(",")]), int(celda_objetivo[celda_objetivo.find(",")+2:len(celda_objetivo)-1]))

        return maze


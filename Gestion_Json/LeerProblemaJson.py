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

        Cnfg.objetivo = (int(celda_objetivo[1]), int(celda_objetivo[4]))

        return (int(celda_inicio[1]), int(celda_inicio[4])), (int(celda_objetivo[1]), int(celda_objetivo[4])), maze


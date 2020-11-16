import json
import Cnfg

class LeerProblemaJson:
    def getData(file_name):

        f = open(file_name, "r")
        content = f.read()
        diccionario = json.loads(content)

        celda_inicio = diccionario["INITIAL"]
        celda_objetivo = diccionario["OBJECTIVE"]
        maze = diccionario["MAZE"]

        Cnfg.objetivo = celda_objetivo

        return celda_inicio, celda_objetivo, maze


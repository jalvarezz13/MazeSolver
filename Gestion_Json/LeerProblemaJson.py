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

        Cnfg.objetivo = celda_objetivo
        print("MODIFICADO EL OBJETIVO: " + str(Cnfg.objetivo), flush=True)
        return celda_inicio, celda_objetivo, maze


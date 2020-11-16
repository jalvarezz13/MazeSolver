import os
import json
import Cnfg


class CrearProblemaJson:

    def __init__(self, inicial, final, maze):
        data = {}
        data["INITIAL"] = inicial
        data["OBJECTIVE"] = final
        data["MAZE"] = maze

        self.file_name = "Problema_B1_2_{0}to{1}.json".format(inicial, final)
        Cnfg.objetivo = final
        with open(os.path.join("{0}/Recursos/JSONs/PROBLEMAs".format(os.getcwd()), self.file_name), 'w') as file:
            json.dump(data, file, indent=4)

    def get_nombre_problema(self):
        return self.file_name

import os
import json
import Cnfg


class CrearProblemaJson:

    def __init__(self, inicial, final, maze):
        self.__inicial = tuple(inicial)
        self.__final = tuple(final)
        self.__maze = maze

        data = {}
        data["INITIAL"] = str(self.__inicial)
        data["OBJETIVE"] = str(self.__final)
        data["MAZE"] = self.__maze
        
        Cnfg.inicial = self.__inicial
        Cnfg.objetivo = self.__final
        
        self.file_name = "Problema_B1_2_{0}to{1}.json".format(self.__inicial, self.__final)

        with open(os.path.join("{0}/Recursos/JSONs/PROBLEMAs".format(os.getcwd()), self.file_name), 'w') as file:
            json.dump(data, file, indent=4)

    def get_nombre_problema(self):
        return self.file_name

    def get_datos_problema(self):
        return [self.__inicial, self.__final]

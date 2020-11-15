import os
import json
import Cnfg

class CrearProblemaJson:

    def __init__(self, inicial, final, maze):
        data = {}
        data["INITIAL"] = inicial
        data["OBJECTIVE"] = final
        data["MAZE"] = maze

        file_name = "Problema_B1_2_{0}to{1}.json".format(inicial, final)

        Cnfg.objetivo = final
        print("MODIFICADO EL OBJETIVO: " + str(Cnfg.objetivo), flush=True)
        with open(os.path.join("{0}/JSONs/PROBLEMAs".format(os.getcwd()), file_name), 'w') as file:
            json.dump(data, file, indent=4)

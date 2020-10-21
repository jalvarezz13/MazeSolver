import os
import json

class ProblemaJson:

    def __init__(inicial, final, maze):           
        data = {}
        data["INITIAL"] = inicial
        data["OBJECTIVE"] = final
        data["MAZE"] = maze
    
        file_name = "Problema_B1_2_{0}to{1}.json".format(inicial, final)

        with open(os.path.join("{0}/JSONs".format(os.getcwd()), maze), 'w') as file:
            json.dump(data, file)
                
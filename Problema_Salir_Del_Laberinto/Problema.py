class Problema:
    def generarSucesores(diccionario):
        file = open("SUCESORs/sucesors_{0}X{1}_funcion.txt".format(diccionario["rows"], diccionario["cols"]), "w")
        sucesores = ""
        tupla = []

        for i in range(0, diccionario["rows"]):
            for j in range(0, diccionario["cols"]):
                sucesores += "SUC(" + "({0}, {1})".format(i, j) + ")="
                tupla.clear()
                for z in range(0, 4):
                    if diccionario["cells"]["({0}, {1})".format(i, j)]["neighbors"][z]:
                        coordFila = i + diccionario["mov"][z][0]
                        coordCol = j + diccionario["mov"][z][1]
                        tupla.append((diccionario["id_mov"][z], "({0}, {1})".format(coordFila, coordCol), 1))
                sucesores += str(tupla) + "\n"

        file.write(sucesores)
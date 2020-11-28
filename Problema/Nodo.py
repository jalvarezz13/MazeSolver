from Problema.Estado import Estado
import Cnfg

class Nodo:

    def __init__(self, id, estado, padre, accion):
        self.__id = id
        self.__nodoPadre = padre
        self.__estado = estado
        self.__accion = accion
        self.__heuristica = self.calcularHeuristica(tuple(Cnfg.objetivo))

        if self.__nodoPadre is None:
            self.__costo = 0
            self.__profundidad = 0
        else:
            self.__costo = padre.getCosto() + accion[2] + 1
            self.__profundidad = padre.getProfundidad() + 1

        self.__valor = self.generarValor(Cnfg.estrategia)

    def generarValor(self, estrategia):
        if estrategia == 1:  # Profundidad
            self.__valor = 1/(self.__profundidad+1)
        elif estrategia == 2:  # Anchura
            self.__valor = self.__profundidad
        elif estrategia == 3:  # Voraz
            self.__valor = self.__heuristica
        elif estrategia == 4:  # Costo uniforme
            self.__valor = self.__costo
        else:   # A*
            self.__valor = self.__costo + self.__heuristica

        return self.__valor

    def getIdNodo(self):
        return self.__id

    def getPadre(self):
        return self.__nodoPadre

    def getIdPadre(self):
        if self.getPadre() is None:
            return None
        else:
            return self.getPadre().getIdNodo()

    def getAccion(self):
        if self.__accion is None:
            return None
        else:
            return self.__accion[0]

    def getEstado(self):
        return self.__estado

    def getHeuristica(self):
        return self.__heuristica

    def getCosto(self):
        return self.__costo

    def getProfundidad(self):
        return self.__profundidad

    def getValor(self):
        return self.__valor
    
    def calcularHeuristica(self, destino):
        return abs(int(self.__estado.getId()[0])-int(destino[0])) + abs(int(self.__estado.getId()[1])-int(destino[1]))

    def generarSucesores(self, diccionario):
        file = open("Recursos/TXTs/SUCESORs/sucesors_{0}X{1}_funcion_{2}.txt".format(diccionario["rows"], diccionario["cols"], str(Cnfg.estrategiaName)), "a")

        lista_sucesores = []
        lista_fichero = []
        estado = self.getEstado()

        i = estado.getId()[0]
        j = estado.getId()[1]

        sucesores = "SUC(" + "({0}, {1})".format(i, j) + ")="

        for z in range(0, 4):
            if diccionario["cells"]["({0}, {1})".format(i, j)]["neighbors"][z]:
                coordFila = i + diccionario["mov"][z][0]
                coordCol = j + diccionario["mov"][z][1]
                lista_sucesores.append((diccionario["id_mov"][z], (coordFila, coordCol), diccionario["cells"]["({0}, {1})".format(coordFila, coordCol)]["value"]))
                lista_fichero.append((diccionario["id_mov"][z], "({0}, {1})".format(coordFila, coordCol), diccionario["cells"]["({0}, {1})".format(coordFila, coordCol)]["value"]))
        sucesores += str(lista_fichero) + "\n"

        file.write(sucesores)

        return lista_sucesores


    def toString(self):

        return("[{0}][{1},{2},{3},{4},{5},{6},{7}]".format(self.getIdNodo(), self.getCosto(),
                                                                  self.getEstado().getId(), self.getIdPadre(),
                                                                  self.getAccion(), self.getProfundidad(),
                                                                  self.getHeuristica(), self.getValor()))

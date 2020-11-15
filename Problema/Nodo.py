from Problema.Estado import Estado
import Cnfg

class Nodo:

    def __init__(self, id, costoAcumulado, estado, padre, accion, heuristica, estrategia):
        self.__id = id
        self.__nodoPadre = padre
        self.__estado = estado
        self.__accion = accion # [mov, id_destino, coste]
        self.__heuristica = self.calcularHeuristica(Cnfg.objetivo, id)

        if self.__nodoPadre == None:
            self.__costoAcumulado = 0
            self.__profundidad = 0
        else:
            # Supones que será un entero siempre
            self.__costoAcumulado = padre.getCosto() + accion[2] + 1
            self.__profundidad = padre.getProfundidad() + 1

        self.__valor = self.generarValor(estrategia)

    def generarValor(self, estrategia):
        if estrategia == 1:  # Profundidad
            self.__valor = 1/(self.__profundidad+1)
        elif estrategia == 2:  # Anchura
            self.__valor = self.__profundidad
        elif estrategia == 3:  # Voraz
            self.__valor = self.__heuristica
        elif estrategia == 4:  # Costo uniforme
            self.__valor = self.__costoAcumulado
        else:   # A*
            self.__valor = self.__costoAcumulado + self.__heuristica

        return self.__valor

    def getIdNodo(self):
        return self.__id

    def getPadre(self):
        return self.__nodoPadre

    def getAccion(self):
        return self.__accion

    def getEstado(self):
        return self.__estado

    def getHeuristica(self):
        return self.__heuristica

    def getCosto(self):
        return self.__costoAcumulado

    def getProfundidad(self):
        return self.__profundidad

    def getValor(self):
        return self.__valor
    
    def calcularHeuristica(self, destino, actual):
        heuristica = (abs(actual[0]-destino[0]) + abs(actual[0]-destino[0]))
        return heuristica

    def generarSucesores(self, diccionario, frontera):
        file = open("Recursos/SUCESORs/sucesors_{0}X{1}_funcion.txt".format(
            diccionario["rows"], diccionario["cols"]), "a")
        sucesores = ""
        tupla = []
        estado = self.getEstado()

        i = estado.getId()[0]
        j = estado.getId()[1]

        sucesores = "SUC(" + "({0}, {1})".format(i, j) + ")="

        for z in range(0, 4):
            nodo = None
            if diccionario["cells"]["({0}, {1})".format(i, j)]["neighbors"][z]:
                coordFila = i + diccionario["mov"][z][0]
                coordCol = j + diccionario["mov"][z][1]
                estado = Estado(coordFila, coordCol)
                nodo = Nodo(0, 0, estado, self, 1, 1, 0)
                frontera.insertar(nodo)
                tupla.append((diccionario["id_mov"][z], "({0}, {1})".format(coordFila, coordCol), 1))
        sucesores += str(tupla) + "\n"

        file.write(sucesores)

    def toString(self):
        return (self.getIdNodo(), self.getCosto(), self.getEstado().getId(), self.getPadre(), self.getAccion(),
                self.getProfundidad(), self.getHeuristica(), self.getValor())

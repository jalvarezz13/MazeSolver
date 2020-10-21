class Nodo:
    def __init__(self, id, costoAcumulado, estado, padre, accion, heuristica, estrategia):
        self.__id = id
        self.__nodoPadre = padre
        self.__estado = estado
        self.__accion = accion
        self.__heuristica = heuristica

        if self.__nodoPadre == None:
            self.__costoAcumulado = 0
            self.__profundidad = 0
        else:
            # Supones que será un entero siempre
            self.__costoAcumulado = padre.getCosto() + costoAcumulado
            self.__profundidad = padre.getProfundidad() + 1

        self.__valor = self.generarValor(estrategia)

    def generarValor(self, estrategia):
        return True  # Modificará la variable valor

    def getIdNodo(self):
        return self.__id

    def getPadre(self):
        return self.__nodoPadre

    def getAccion(self):
        return self.__accion

    def getHeuristica(self):
        return self.__heuristica

    def getCosto(self):
        return self.__costoAcumulado

    def getProfundidad(self):
        return self.__profundidad

    def getValor(self):
        return self.__valor

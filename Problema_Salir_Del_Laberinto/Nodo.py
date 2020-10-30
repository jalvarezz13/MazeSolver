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
        if estrategia == 1:  # Profundidad
            self.__valor = 1/(self.__profundidad+1)
        elif estrategia == 2: # Anchura
            self.__valor = self.__profundidad
        elif estrategia == 3: # Voraz
            self.__valor = self.__heuristica
        elif estrategia == 4: # Costo uniforme
            self.__valor = self.__costoAcumulado
        else:   # A*
            self.__valor = self.__costoAcumulado + self.__heuristica

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

    def generarSucesores(diccionario, matriz):
        print(diccionario)
        print("\n--------------------------------------------\n")
        print(matriz)
        # file = open("sucesors_{0}X{1}_funcion.txt".format())
        # return True # CREAR
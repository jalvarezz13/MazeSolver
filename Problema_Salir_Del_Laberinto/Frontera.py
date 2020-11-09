class Frontera:
    def CreaFrontera(self):
        frontera = []
        return frontera

    def __init__(self):
        self.__listaFrontera = self.CreaFrontera()

    def insertar(self, nodoArbol, estado):
        self.__listaFrontera.append(nodoArbol)
        #id = (estado.getId()[0], estado.getId()[1])
        #idToString = [nodoArbol.getValor(), id]

        self.__listaFrontera.sort(key=lambda nodoArbol: (nodoArbol.getValor(), nodoArbol.getEstado().getId()[0], nodoArbol.getEstado().getId()[1]))

    def elimina(self):  # Devuelve y elimina el  nodo con menos valor
        return self.__listaFrontera.pop(0)

    def esVacia(self):
        return self.__listaFrontera == []

    def getFrontera(self):
        return self.__listaFrontera

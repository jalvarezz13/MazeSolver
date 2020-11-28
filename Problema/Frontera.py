class Frontera:

    def __init__(self):
        frontera = []
        self.__listaFrontera = frontera

    def insertar(self, nodoArbol):
        self.__listaFrontera.append(nodoArbol)
        self.__listaFrontera.sort(key=lambda nodoArbol: (nodoArbol.getValor(), nodoArbol.getEstado().getId()[0], nodoArbol.getEstado().getId()[1], nodoArbol.getIdNodo()))

    def getPrimerElemento(self):
        return self.__listaFrontera.pop(0)

    def esVacia(self):
        return self.__listaFrontera == []

    def getFrontera(self):
        return self.__listaFrontera

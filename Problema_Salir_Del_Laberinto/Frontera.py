class Frontera:
    def CreaFrontera(self):
        frontera = []
        return frontera

    def __init__(self):
        self.__listaFrontera = self.CreaFrontera()

    def insertar(self, nodoArbol, estado):
        self.__listaFrontera.append(nodoArbol)
        print("({0}, {1})".format(estado.getId()[0], estado.getId()[1]))

        def sort_key():
            return tuple(nodoArbol.getValor(), estado.getId()[0], estado.getId()[1])

        self.__listaFrontera.sort(key=sort_key())

    def elimina(self):  # Devuelve y elimina el  nodo con menos valor
        return self.__listaFrontera.pop(0)

    def esVacia(self):
        return self.__listaFrontera == []

    def getFrontera(self):
        return self.__listaFrontera

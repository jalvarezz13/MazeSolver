class Frontera:
    def CreaFrontera(self):
        frontera = []
        return frontera

    def __init__(self):
        self.__listaFrontera=self.CreaFrontera()

    def insertar(self, nodoArbol):
        self.__listaFrontera.append(nodoArbol)
        self.__listaFrontera.sort(self.__listaFrontera, key= lambda Nodo: (Nodo.getValor(), Nodo.getIdNodo())) # Revisar KEY
    
    def elimina(self): # Devuelve y elimina el  nodo con menos valor
        return self.__listaFrontera.pop(0)

    def esVacia(self):
        return self.__listaFrontera == []
from Problema.Nodo import Nodo
from Problema.Frontera import Frontera
from Problema.Estado import Estado
import Cnfg


class Busqueda:

    def __init__(self, problema):
        self.inicio = problema[0]
        self.objetivo = problema[1]
        self.diccionario = problema[2]
        self.camino = []

    def get_camino(self):
        return self.camino

    def generar_camino(self, nodo):
        while nodo.getPadre() is not None:
            self.camino.append(nodo)
            nodo = nodo.getPadre()

        self.camino.append(nodo)

        self.camino.reverse()

    def obtenerIDs(self):
        listaIDs = []
        for i in range(0, len(self.camino)):
            nodo = self.camino[i]
            listaIDs.append(nodo.getEstado().getId())

        return listaIDs


    def algoritmoBusqueda(self):
        visitados = set()
        frontera = Frontera()
        id = 0
        estado = Estado(self.inicio[0], self.inicio[1])
        padre = None
        accion = None
        nodo = Nodo(id, estado, padre, accion)
        
        # visitados.add(nodo.getEstado().getId())
        frontera.insertar(nodo)
        solucion = False

        while not frontera.esVacia() and not solucion:
            nodo = frontera.getPrimerElemento()
            if self.objetivo[0] == nodo.getEstado().getId()[0] and self.objetivo[1] == nodo.getEstado().getId()[1]:
                solucion = True

            elif nodo.getEstado().getId() not in visitados and nodo.getProfundidad() < Cnfg.profundidad:
                visitados.add(nodo.getEstado().getId())
                lista_sucesores = nodo.generarSucesores(self.diccionario)
                print(lista_sucesores)
                for sucesor in lista_sucesores:
                    id += 1
                    estado = Estado(sucesor[1][0], sucesor[1][1])
                    nodo_hijo = Nodo(id, estado, nodo, sucesor)
                    frontera.insertar(nodo_hijo)

        if solucion:
            self.generar_camino(nodo)

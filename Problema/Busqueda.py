from Problema.Nodo import Nodo
from Problema.Frontera import Frontera
from Problema.Estado import Estado
import Cnfg


class Busqueda:

    def __init__(self, dict_manual):
        self.diccionario = dict_manual
        self.inicio = tuple(Cnfg.inicial)
        self.objetivo = tuple(Cnfg.objetivo)
        self.estrategia = Cnfg.estrategia
        self.camino = []
        self.visitados = set()
        self.frontera = Frontera()

    def get_camino(self):
        return self.camino

    def generar_camino(self, nodo):
        while nodo.getPadre() is not None:
            self.camino.append(nodo)
            nodo = nodo.getPadre()

        self.camino.append(nodo)
        self.camino.reverse()

        file = open("Recursos/TXTs/SOLUTIONs/Solucion_{0}to{1}_{2}.txt".format(self.inicio, self.objetivo, Cnfg.estrategiaName), "w+")

        file.write("[id][cost,state,father_id,action,depth,h,value]")
        
        for i in range(0, len(self.camino)):
            file.write("\n" + self.camino[i].toString())

        file.close

    def getVisitados(self):
        return self.visitados

    def getFrontera(self):
        listaFrontera = []
        for i in range(0, len(self.frontera.getFrontera())):
            nodo = self.frontera.getFrontera()[i]
            listaFrontera.append(nodo.getEstado().getId())

        return listaFrontera

    def obtenerNodos(self):
        listaNodos = []
        for i in range(0, len(self.camino)):
            nodo = self.camino[i]
            listaNodos.append(nodo.getEstado().getId())

        return listaNodos


    def algoritmoBusqueda(self):
        id = 0
        estado = Estado(self.inicio[0], self.inicio[1])
        padre = None
        accion = None
        nodo = Nodo(id, estado, padre, accion)        

        self.frontera.insertar(nodo)
        solucion = False

        while not self.frontera.esVacia() and not solucion:
            nodo = self.frontera.getPrimerElemento()
            if self.objetivo[0] == nodo.getEstado().getId()[0] and self.objetivo[1] == nodo.getEstado().getId()[1]:
                solucion = True

            elif nodo.getEstado().getId() not in self.visitados and nodo.getProfundidad() < Cnfg.profundidad:
                self.visitados.add(nodo.getEstado().getId())
                lista_sucesores = nodo.generarSucesores(self.diccionario)
                for sucesor in lista_sucesores:
                    id += 1
                    estado = Estado(sucesor[1][0], sucesor[1][1])
                    nodo_hijo = Nodo(id, estado, nodo, sucesor)
                    self.frontera.insertar(nodo_hijo)

        if solucion:
            self.generar_camino(nodo)

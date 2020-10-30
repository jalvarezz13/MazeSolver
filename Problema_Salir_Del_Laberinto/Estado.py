class Estado:
    def __init__(self, fila, columna, mov, costeMovimiento):
        self.__id = (self.fila, self.columna)

    def getId(self):
        return self.__id
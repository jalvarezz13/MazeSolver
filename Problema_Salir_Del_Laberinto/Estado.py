class Estado:
    def __init__(self, fila, columna):
        self.__id = (self.fila, self.columna)

    def getId(self):
        return self.__id

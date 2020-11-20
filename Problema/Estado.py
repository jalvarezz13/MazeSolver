class Estado:
    def __init__(self, fila, columna):
        self.__id = fila, columna

    def getId(self):
        return self.__id


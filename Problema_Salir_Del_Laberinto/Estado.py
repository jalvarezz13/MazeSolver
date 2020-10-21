class Estado:
    def __init__(self, fila, columna, mov, costeMovimiento):
        self.__id = (self.fila, self.columna)
        self.__mov = mov
        self.__CosteMovimiento = costeMovimiento

    def getId(self):
        return self.__id

    def getMov(self):
        return self.__mov
    
    def getCosto(self):
        return self.__CosteMovimiento

    

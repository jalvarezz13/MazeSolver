class Cell:
    def __init__(self, row, column, value, neighbors):
        self.row = row
        self.column = column
        self.value = value
        self.neighbors = neighbors
        self.visited = False

    def get_row (self):
        return self.row

    def get_column(self):
        return self.column

    def get_coordenadas(self):
        return self.row, self.column

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def get_visited(self):
        return self.visited
    
    def set_visited(self, valor):
        self.visited = valor

    def esPared(celda, movimiento, lab):
        esPared = False
        if celda.get_row() == 0 and movimiento == [-1, 0]:
            esPared = True
        if celda.get_column() == 0 and movimiento == [0, -1]:
            esPared = True
        if celda.get_row() == lab.get_rows() - 1 and movimiento == [1, 0]:
            esPared = True
        if celda.get_column() == lab.get_cols() - 1 and movimiento == [0, 1]:
            esPared = True
        return esPared

    def to_string(self):
        return ("Fila: '{0}' \nColumna: '{1}' \nValor: '{2}' \nVecinos: '{3}' \n".format(self.row, self.column, self.value, self.neighbors))
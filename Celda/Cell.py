
class Cell:
    def __init__(self, row, column, value, neighbors):
        #fila y columna en la que se encuentra la celda, podria ponerse como tupla
        self.row = row
        self.column = column
        self.value = value
        self.neighbors = neighbors
        self.visited = False

    def get_row (self):
        return self.row

    def get_column(self):
        return self.column

    def get_value(self):
        return self.value

    def get_neighbors(self):
        return self.neighbors

    def get_visited(self):
        return self.visited
    
    def set_visited(self, valor):
        self.visited = valor

    def to_string(self):
        return ("Fila: '{0}' \nColumna: '{1}' \nValor: '{2}' \nVecinos: '{3}' \n".format(self.row, self.column, self.value, self.neighbors))
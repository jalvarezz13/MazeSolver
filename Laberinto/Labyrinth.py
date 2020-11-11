from Laberinto.Cell import Cell
import json
import numpy

class Labyrinth:
    def __init__(self, path=None, rows=None, cols=None):
        if path is not None:
            with open(path) as file:
                self.dict_data = json.load(file)
                self.rows = int(self.dict_data["rows"])
                self.cols = int(self.dict_data["cols"])
        else:
            self.rows = rows
            self.cols = cols

        self.labyrinth = None

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_labyrinth(self):
        return self.labyrinth

    def create_labyrinth(self):
        self.labyrinth = numpy.empty([self.rows, self.cols], dtype=object)

    def load_data(self, dic_data_manual):
        if self.labyrinth is None:
            cells = (self.dict_data["cells"])
            self.create_labyrinth()

        else:
            cells = dic_data_manual["cells"]

        for i in range(0, self.get_rows()):
            for j in range(0, self.get_cols()):
                coordenadas = cells["({0}, {1})".format(i, j)]
                cell = Cell(i, j, coordenadas["value"], coordenadas["neighbors"])
                self.labyrinth[i][j] = cell

    def generar_celdas_no_visitadas(matriz_laberinto, lab):
        no_visitadas = []
        for i in range(0, lab.get_rows()):
            for j in range(0, lab.get_cols()):
                if matriz_laberinto[i][j].get_visited() is False:
                    no_visitadas.append(matriz_laberinto[i][j])

        return no_visitadas
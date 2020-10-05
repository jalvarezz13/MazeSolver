import json

from Celda.Cell import Cell
import cnfg
import numpy as np
import pygame


class Labyrinth:
    def __init__(self, path=None):
        if path is not None:
            with open(path) as file:
                self.dict_data = json.load(file)
        self.labyrinth = None

    def get_rows(self):
        return int(self.dict_data["rows"])

    def get_cols(self):
        return int(self.dict_data["cols"])

    def get_labyrinth(self):
        return self.labyrinth

    def create_labyrinth(self):
        self.labyrinth = np.empty([int(self.dict_data["rows"]), int(self.dict_data["cols"])], dtype=object)

    def load_data(self):
        cells = (self.dict_data["cells"])

        self.create_labyrinth()

        for i in range(0, self.get_rows()):
            for j in range(0, self.get_cols()):
                coordenadas = cells["({0}, {1})".format(i, j)]
                cell = Cell(i, j, coordenadas["value"], coordenadas["neighbors"])
                self.labyrinth[i][j] = cell
                # Solo para comprobar que se crea, aqui no deberia ir
                # print(cell.to_string())

    def dibujar(self, screen):
        if self.get_rows() > self.get_cols():
            w = int(cnfg.ancho / self.get_rows())
        else:
            w = int(cnfg.alto / self.get_cols())

        y = -w + 20

        for i in range(0, self.get_rows()):
            # set x coordinate to start position
            x = 20
            y = y + w
            for j in range(0, self.get_cols()):
                cell = self.labyrinth[i][j]
                vecinos = cell.get_neighbors()
                # top of cell
                if not vecinos[0]:
                    pygame.draw.line(screen, cnfg.BLACK, [x, y], [x + w, y])

                # right of cell
                if not vecinos[1]:
                    pygame.draw.line(screen, cnfg.BLACK, [x + w, y], [x + w, y + w])

                # bottom of cell
                if not vecinos[2]:
                    pygame.draw.line(screen, cnfg.BLACK, [x + w, y + w], [x, y + w])

                # left of cell
                if not vecinos[3]:
                    pygame.draw.line(screen, cnfg.BLACK, [x, y + w], [x, y])
                x = x + w

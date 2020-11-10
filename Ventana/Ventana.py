import pygame
import Cnfg

def dibujarLineas(screen, lab):
    if lab.get_rows() > lab.get_cols():
        w = int(Cnfg.ancho / lab.get_rows())
    else:
        w = int(Cnfg.alto / lab.get_cols())
    y = -w + 20

    if(lab.get_rows() >= 75 or lab.get_cols() >= 75):
        Cnfg.anchoLinea -= 1

    for i in range(0, lab.get_rows()):
        x = 20
        y = y + w

        for j in range(0, lab.get_cols()):
            cell = lab.labyrinth[i][j]
            vecinos = cell.get_neighbors()

            if not vecinos[0]:
                pygame.draw.line(screen, Cnfg.BLACK, [x, y], [x + w, y], Cnfg.anchoLinea)

            if not vecinos[1]:
                pygame.draw.line(screen, Cnfg.BLACK, [x + w, y], [x + w, y + w], Cnfg.anchoLinea)

            if not vecinos[2]:
                pygame.draw.line(screen, Cnfg.BLACK, [x + w, y + w], [x, y + w], Cnfg.anchoLinea)

            if not vecinos[3]:
                pygame.draw.line(screen, Cnfg.BLACK, [x, y + w], [x, y], Cnfg.anchoLinea)
            x = x + w

def dibujarColores(screen, lab):
    if lab.get_rows() > lab.get_cols():
        w = int(Cnfg.ancho / lab.get_rows())
    else:
        w = int(Cnfg.alto / lab.get_cols())
    y = -w + 20

    for i in range(0, lab.get_rows()):
        x = 20
        y = y + w

        for j in range(0, lab.get_cols()):
            cell = lab.labyrinth[i][j]
            value = cell.get_value()

            if value == 0:
                pygame.draw.rect(screen, Cnfg.ASPHALT, [x, y, w, w], 0)

            if value == 1:
                pygame.draw.rect(screen, Cnfg.GROUND, [x, y, w, w], 0)

            if value == 2:
                pygame.draw.rect(screen, Cnfg.GRASS, [x, y, w, w], 0)

            if value == 3:
                pygame.draw.rect(screen, Cnfg.WATER, [x, y, w, w], 0)
            x = x + w

class Ventana:
    def dibujar (screen, lab):
        dibujarColores(screen, lab)
        dibujarLineas(screen, lab)

    def inicializar_ventana(lab):
        pygame.init()
        if lab.get_rows() > lab.get_cols():
            w = Cnfg.ancho / lab.get_rows()
        else:
            w = Cnfg.alto / lab.get_cols()

        new_ancho = int(w * lab.get_cols() + 40)
        new_alto = int(w * lab.get_rows() + 40)

        screen = pygame.display.set_mode((new_ancho, new_alto))
        pygame.display.set_caption("Laberinto de Sistemas Inteligentes B1_2")

        return screen
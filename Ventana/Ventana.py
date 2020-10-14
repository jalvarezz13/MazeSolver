import pygame
import Cnfg

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

def dibujar(screen, lab):
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
            vecinos = cell.get_neighbors()

            if not vecinos[0]:
                pygame.draw.line(screen, Cnfg.BLACK, [x, y], [x + w, y])

            if not vecinos[1]:
                pygame.draw.line(screen, Cnfg.BLACK, [x + w, y], [x + w, y + w])

            if not vecinos[2]:
                pygame.draw.line(screen, Cnfg.BLACK, [x + w, y + w], [x, y + w])

            if not vecinos[3]:
                pygame.draw.line(screen, Cnfg.BLACK, [x, y + w], [x, y])
            x = x + w


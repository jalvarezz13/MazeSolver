import pygame
import cnfg

def inicializar_ventana(lab):
    pygame.init()
    if lab.get_rows() > lab.get_cols():
        w = cnfg.ancho / lab.get_rows()  # Para que dentro de la venta 500x500 salgan las celdas lo más grande posible
    else:
        w = cnfg.alto / lab.get_cols()

    # Hacemos que el tamaño de la ventana se ajuste por ejemplo laberintos de 2*8
    new_ancho = int(w * lab.get_cols() + 40)
    new_alto = int(w * lab.get_rows() + 40)

    screen = pygame.display.set_mode((new_ancho, new_alto))
    pygame.display.set_caption("Laberinto de Sistemas Inteligentes")

    return screen

def dibujar(screen, lab):
    if lab.get_rows() > lab.get_cols():
        w = int(cnfg.ancho / lab.get_rows())
    else:
        w = int(cnfg.alto / lab.get_cols())

    y = -w + 20

    for i in range(0, lab.get_rows()):
        # set x coordinate to start position
        x = 20
        y = y + w
        for j in range(0, lab.get_cols()):
            cell = lab.labyrinth[i][j]
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


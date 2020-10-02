import sys
from Laberinto.Labyrinth import Labyrinth
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


lab = Labyrinth("prueba.json")
lab.load_data()
#lab.check_json()
screen = inicializar_ventana(lab)


while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            name = "Laberinto_B02_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
            pygame.image.save(screen, name)
            sys.exit()

    screen.fill(cnfg.WHITE)
    lab.dibujar(screen)
    pygame.display.update()




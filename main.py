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


def algoritmo_wilson(rows_cols):
    return True


def pedir_nombre_fichero():
    valido = False
    while not valido:
        try:
            nombre_fichero = input("introduce el nombre del fichero con extensión .json:\n")
            lab = Labyrinth(nombre_fichero)
            valido = True
        except FileNotFoundError:
            print("\nNo se ha encontrado el archivo, vuelve a intentarlo\n")

    return lab


def pedir_filas_columnas():
    rows_cols = []
    valido = False
    data = "fila"
    while not valido and len(rows_cols) != 2:
        try:
            rows_cols.append(int(input("\nIntroduce el número de {0}: ".format(data))))
            data = "columna"
        except ValueError:
            print("\nIntroduce un número válido\n")


def main():
    valido = False
    while not valido:
        try:
            option = int(input(
                "Elige una opción [1,2]:\n\t1. Elegir archivo existente\n\t2. Generar algoritmo automáticamente\n\n"))
            if option == 1:
                lab = pedir_nombre_fichero()
                valido = True
            if option == 2:
                rows_cols = pedir_filas_columnas()
                lab = algoritmo_wilson(rows_cols)
                valido = True
            else:
                print("Intruduce un valor válido [1, 2]\n")
                print("ahora aqui")
        except ValueError:
            print("aqui")
            print("Intruduce un valor válido [1, 2]\n")

    screen = inicializar_ventana(lab)
    lab.load_data()

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


if __name__ == '__main__':
    main()

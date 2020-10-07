import sys
from Laberinto.Labyrinth import Labyrinth
import pygame
import cnfg
import io
import os
import json
import random


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

    return rows_cols


def crear_celdas(rows, cols):
    data = {}
    data2 = {}
    for i in range(0, rows):
        for j in range(0, cols):
            data2["value"] = 0
            data2["neighbors"] = [False, False, False, False]
            datos = data2
            data["({0}, {1})".format(i, j)] = datos

    return data


def crear_json(rows, cols):
    data = {}
    data['rows'] = rows
    data['cols'] = cols
    data["max_n"] = 4,
    data["mov"] = [[-1,0], [0,1], [1,0], [0,-1]]
    data["id_mov"] = ["N", "E", "S", "O"]
    data["cells"] = crear_celdas(rows, cols)
    dir = os.getcwd()
    file_name = "Laberinto_wilson_B02_{0}x{1}.json".format(rows, cols)

    with open(os.path.join(dir, file_name), 'w') as file:
        json.dump(data, file)

    return data


def celda_inicial_final(lab, matriz_laberinto):

    y_inicial = random.randrange(0, lab.get_rows())
    x_inicial = random.randrange(0, lab.get_cols())

    y_final = random.randrange(0, lab.get_rows())
    x_final = random.randrange(0, lab.get_cols())

    celda_inicial = matriz_laberinto[y_inicial, x_inicial]
    celda_final = matriz_laberinto[y_final, x_final]

    return [celda_inicial, celda_final]


def algoritmo_wilson(lab, diccionario):
    matriz_laberinto = lab.get_labyrinth()

    celda_inicial, celda_final = celda_inicial_final(lab, matriz_laberinto)





def menu_inicial():
    valido = False
    dict_manual = None
    while not valido:
        try:
            option = int(input(
                "Elige una opción [1,2]:\n\t1. Elegir archivo existente\n\t2. Generar algoritmo automáticamente\n\n"))
            if option == 1:
                lab = pedir_nombre_fichero()
                valido = True
            elif option == 2:
                rows_cols = pedir_filas_columnas()
                lab = Labyrinth(None, rows_cols[0], rows_cols[1])
                lab.create_labyrinth(rows_cols[0], rows_cols[1])
                dict_manual = crear_json(rows_cols[0], rows_cols[1])
                lab.load_data(dict_manual)
                algoritmo_wilson(lab, dict_manual)
                valido = True
            else:
                print("Intruduce un valor válido [1, 2]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2]\n")

    return [lab, dict_manual]


def main():
    lab, dict_data_manual = menu_inicial()
    screen = inicializar_ventana(lab)
    lab.load_data(dict_data_manual)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                name = "Laberinto_B02_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
                pygame.image.save(screen, name)
                sys.exit()

        screen.fill(cnfg.WHITE)
        lab.dibujar(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()

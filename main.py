import sys
from Laberinto.Labyrinth import Labyrinth
import pygame
import cnfg
import os
import json
import random
import numpy


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
    lab = None
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
    dic_cell = {}
    dic_data_cell = {}
    for i in range(0, rows):
        for j in range(0, cols):
            dic_data_cell["value"] = 0
            dic_data_cell["neighbors"] = [False, False, False, False]
            dic_cell["({0}, {1})".format(i, j)] = dic_data_cell
    return dic_cell


def crear_json(rows, cols):
    data = {}
    data["rows"] = rows
    data["cols"] = cols
    data["max_n"] = 4,
    data["mov"] = [[-1,0], [0,1], [1,0], [0,-1]]
    data["id_mov"] = ["N", "E", "S", "O"]
    data["cells"] = crear_celdas(rows, cols)
    file_name = "Laberinto_wilson_B02_{0}x{1}.json".format(rows, cols)

    with open(os.path.join(os.getcwd(), file_name), 'w') as file:
        json.dump(data, file)

    return data


def elegir_movimiento(celda_actual, diccionario, lab):
    num_random = random.randrange(0, 4)
    movimiento = diccionario["mov"][num_random]
    while esPared(celda_actual, movimiento, lab):
        num_random = (num_random + 1) % 4
        movimiento = diccionario["mov"][num_random]

    return [int(movimiento[0]), int(movimiento[1])]

def esPared(celda, movimiento, lab):
    esPared = False
    if celda.get_row() == 0 and movimiento == [-1,0]:
        esPared = True
    if celda.get_column() == 0 and movimiento == [0, -1]:
        esPared = True
    if celda.get_row() == lab.get_rows()-1 and movimiento == [1, 0]:
        esPared = True
    if celda.get_column() == lab.get_cols()-1 and movimiento == [0, 1]:
        esPared = True
    return esPared

def crear_celda_random(lab, matriz_laberinto):
    while True:
        y = random.randrange(0, lab.get_rows())
        x = random.randrange(0, lab.get_cols())
        celda_random = matriz_laberinto[y, x]
        if celda_random.get_visited() is False:
            break
    return celda_random


def check_camino(celda, camino, coord_movimiento, lista_movimientos):
    lista2_mov = []
    if camino.count(celda) != 0:
        lim_superior = len(camino)-1
        lim_inferior = camino.index(celda)+1
        for i in range(lim_superior, lim_inferior-1, -1): #Desde el final hasta la primera repetición de ese bucle
            camino.remove(camino[i])

        for i in range(0, lim_inferior-1):
            lista2_mov.append(lista_movimientos[i])
    else:
        lista_movimientos.append(coord_movimiento)
        camino.append(celda)
        lista2_mov = lista_movimientos

    return camino, lista2_mov

def generar_celdas_visitadas(matriz_laberinto, lab):
    visitadas = []
    no_visitadas = []
    for i in range(0, lab.get_rows()):
        for j in range(0, lab.get_cols()):
            if matriz_laberinto[i][j].get_visited() == True:
                visitadas.append(matriz_laberinto[i][j])
            else:
                no_visitadas.append(matriz_laberinto[i][j])

    return no_visitadas, visitadas


def crear_camino(celda_final, lab, matriz_laberinto, diccionario):
    camino = []
    lista_movimientos = []
    celda_inicial = crear_celda_random(lab, matriz_laberinto)
    camino.append(celda_inicial.get_coordenadas())
    # print("CELDA INICIAL:" + str([celda_inicial.get_row(), celda_inicial.get_column()]))
    celdas_no_visitadas, celdas_visitadas = generar_celdas_visitadas(matriz_laberinto, lab)

    # while len(celdas_no_visitadas) != 1:
    while True:
        posicion = camino[len(camino)-1]
        celda_actual = matriz_laberinto[posicion[0], posicion[1]]

        coord_movimiento = elegir_movimiento(celda_actual, diccionario, lab)
        new_posicion = numpy.array((celda_actual.get_row(), celda_actual.get_column())) + numpy.array((coord_movimiento[0], coord_movimiento[1]))
        new_celda = matriz_laberinto[new_posicion[0], new_posicion[1]]
        camino, lista_movimientos = check_camino(new_celda.get_coordenadas(), camino, coord_movimiento, lista_movimientos)

        ultima_celda_anadida = matriz_laberinto[camino[len(camino)-1][0]][camino[len(camino)-1][1]]
        if ultima_celda_anadida.get_visited() == True:
        # if camino[len(camino)-1][0] == celda_final.get_row() and camino[len(camino)-1][1] == celda_final.get_column():
            # print("TERMINÉ")

            for i in range(0, len(camino)):
                coord = camino[i]
                matriz_laberinto[coord[0]][coord[1]].set_visited(True)
                celdas_no_visitadas, celdas_visitadas = generar_celdas_visitadas(matriz_laberinto, lab)
                # if celdas_no_visitadas.count(str(matriz_laberinto[coord[0]][coord[1]].get_coordenadas())) == 1:
                #     celdas_no_visitadas.remove(str(matriz_laberinto[coord[0]][coord[1]].get_coordenadas()))
                #
                # if celdas_visitadas.count(str(matriz_laberinto[coord[0]][coord[1]].get_coordenadas())) == 0:
                #     celdas_visitadas.append(str(matriz_laberinto[coord[0]][coord[1]].get_coordenadas()))

            diccionario = cambiar_vecinos(camino, lista_movimientos, diccionario)
            celda_inicial = crear_celda_random(lab, matriz_laberinto)
            camino.clear()
            lista_movimientos.clear()
            camino.append(celda_inicial.get_coordenadas())

        celdas_no_visitadas, celdas_visitadas = generar_celdas_visitadas(matriz_laberinto, lab)

        if len(celdas_no_visitadas) == 1:
            celda = celdas_no_visitadas[0]
            coord_movimiento = elegir_movimiento(celda, diccionario, lab)
            new_posicion = numpy.array((celda.get_row(), celda.get_column())) + numpy.array(
                (coord_movimiento[0], coord_movimiento[1]))
            new_celda = matriz_laberinto[new_posicion[0], new_posicion[1]]
            camino, lista_movimientos = check_camino(new_celda.get_coordenadas(), camino, coord_movimiento,
                                                     lista_movimientos)
            diccionario = cambiar_vecinos(camino, lista_movimientos, diccionario)

            break

    return camino, lista_movimientos, diccionario


def cambiar_vecinos(camino, lista_movimientos, diccionario):
    movimiento = diccionario["mov"]
    posicion_vecino = None
    file_name = "Laberinto_wilson_B02_{0}x{1}.json".format(diccionario["rows"], diccionario["cols"])

    f = open(file_name, "r")
    content = f.read()
    diccionario = json.loads(content)

    for i in range(0, (len(camino)-1)):
        if lista_movimientos[i] == movimiento[0]:
            posicion_vecino = 0
        elif lista_movimientos[i] == movimiento[1]:
            posicion_vecino = 1
        elif lista_movimientos[i] == movimiento[2]:
            posicion_vecino = 2
        elif lista_movimientos[i] == movimiento[3]:
            posicion_vecino = 3

        diccionario["cells"][str(camino[i])]["neighbors"][posicion_vecino] = True
        diccionario["cells"][str(camino[i + 1])]["neighbors"][(posicion_vecino + 2) % 4] = True

    with open(file_name, 'r+') as f:
        f.seek(0)
        f.write(json.dumps(diccionario))
        f.truncate()

    f = open(file_name, "r")
    content = f.read()
    diccionario = json.loads(content)

    return diccionario


def algoritmo_wilson(lab, diccionario):
    matriz_laberinto = lab.get_labyrinth()
    celda_final = crear_celda_random(lab, matriz_laberinto)
    celda_final.set_visited(True)
    # print("CELDA FINAL:" + str([celda_final.get_row(), celda_final.get_column()]))
    print("Generando laberinto...")
    camino, lista_movimientos, diccionario = crear_camino(celda_final, lab, matriz_laberinto, diccionario)

    return diccionario 


def menu_inicial():
    valido = False
    dict_manual = None
    lab = None
    while not valido:
        try:
            option = int(input("Elige una opción [1,2]:\n\t1. Elegir archivo existente\n\t2. Generar algoritmo automáticamente\n\n"))
            if option == 1:
                lab = pedir_nombre_fichero()
                lab.load_data(None)
                valido = True
            elif option == 2:
                rows_cols = pedir_filas_columnas()
                lab = Labyrinth(None, rows_cols[0], rows_cols[1])
                lab.create_labyrinth()
                dict_manual = crear_json(rows_cols[0], rows_cols[1])
                lab.load_data(dict_manual)
                dict_manual = algoritmo_wilson(lab, dict_manual)
                lab.load_data(dict_manual)
                valido = True
            else:
                print(" ELSE Intruduce un valor válido [1, 2]\n")
        except ValueError:
            print(ValueError.__cause__)
            print("VALUE Intruduce un valor válido [1, 2]\n")

    return [lab, dict_manual]


def main():
    lab, dict_data_manual = menu_inicial()
    screen = inicializar_ventana(lab)

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

from Laberinto.Cell import Cell
from Laberinto.Labyrinth import Labyrinth
from Gestion_Json.LaberintoJson import LaberintoJson
import random
import numpy

class AlgoritmoWilson:
    def elegir_movimiento(celda_actual, diccionario, lab):
        num_random = random.randrange(0, 4)
        movimiento = diccionario["mov"][num_random]

        while Cell.esPared(celda_actual, movimiento, lab):
            num_random = (num_random + 1) % 4
            movimiento = diccionario["mov"][num_random]

        return [int(movimiento[0]), int(movimiento[1])]

    def crear_celda_random(lab, matriz_laberinto, celdas_no_visitadas=None):
        while True:
            if celdas_no_visitadas is None:
                y = random.randrange(0, lab.get_rows())
                x = random.randrange(0, lab.get_cols())
                celda_random = matriz_laberinto[y, x]

            else:
                celda_random = random.choice(celdas_no_visitadas)

            if celda_random.get_visited() is False:
                break

        return celda_random

    def check_camino(celda, camino, coord_movimiento, lista_movimientos):
        lista2_mov = []
        if camino.count(celda) != 0:
            lim_superior = len(camino) - 1
            lim_inferior = camino.index(celda) + 1
            for i in range(lim_superior, lim_inferior - 1, -1):
                camino.remove(camino[i])

            for i in range(0, lim_inferior - 1):
                lista2_mov.append(lista_movimientos[i])
        else:
            lista_movimientos.append(coord_movimiento)
            camino.append(celda)
            lista2_mov = lista_movimientos

        return camino, lista2_mov

    def iniciar_algoritmo(matriz_laberinto, lab):
        camino = []
        celdas_no_visitadas = Labyrinth.generar_celdas_no_visitadas(matriz_laberinto, lab)
        celda_inicial = AlgoritmoWilson.crear_celda_random(lab, matriz_laberinto, celdas_no_visitadas)
        camino.append(celda_inicial.get_coordenadas())

        return camino, celdas_no_visitadas

    def calcular_caminos(camino, lista_movimientos, matriz_laberinto, diccionario, lab):
        posicion = camino[len(camino) - 1]
        celda_actual = matriz_laberinto[posicion[0], posicion[1]]
        coord_movimiento = AlgoritmoWilson.elegir_movimiento(celda_actual, diccionario, lab)
        new_posicion = numpy.array((celda_actual.get_row(), celda_actual.get_column())) + numpy.array(
            (coord_movimiento[0], coord_movimiento[1]))
        new_celda = matriz_laberinto[new_posicion[0], new_posicion[1]]
        camino, lista_movimientos = AlgoritmoWilson.check_camino(new_celda.get_coordenadas(), camino, coord_movimiento,
                                                lista_movimientos)

        return camino, lista_movimientos, new_celda

    def actualizar_celdas(camino, matriz_laberinto, celdas_no_visitadas, lista_movimientos, diccionario):
        for i in range(0, len(camino)):
            coord = camino[i]
            matriz_laberinto[coord[0]][coord[1]].set_visited(True)

            if celdas_no_visitadas.count(matriz_laberinto[coord[0]][coord[1]]) == 1:
                celdas_no_visitadas.remove(matriz_laberinto[coord[0]][coord[1]])

        diccionario = LaberintoJson.cambiar_vecinos(camino, lista_movimientos, diccionario)

        return celdas_no_visitadas, diccionario

    def generar_laberinto(lab, matriz_laberinto, diccionario):
        lista_movimientos = []
        camino, celdas_no_visitadas = AlgoritmoWilson.iniciar_algoritmo(matriz_laberinto, lab)

        while True:
            camino, lista_movimientos, new_celda = AlgoritmoWilson.calcular_caminos(camino, lista_movimientos, matriz_laberinto, diccionario, lab)
            if new_celda.get_visited():
                celdas_no_visitadas, diccionario = AlgoritmoWilson.actualizar_celdas(camino, matriz_laberinto, celdas_no_visitadas, lista_movimientos, diccionario)
                if len(celdas_no_visitadas) == 0:
                    print("Terminé")
                    break
                celda_inicial = AlgoritmoWilson.crear_celda_random(lab, matriz_laberinto, celdas_no_visitadas)
                camino.clear()
                lista_movimientos.clear()
                camino.append(celda_inicial.get_coordenadas())

        return camino, lista_movimientos, diccionario

    def algoritmo_wilson(lab, diccionario):
        matriz_laberinto = lab.get_labyrinth()
        celda_final = AlgoritmoWilson.crear_celda_random(lab, matriz_laberinto)
        celda_final.set_visited(True)
        print("Generando laberinto...")
        camino, lista_movimientos, diccionario = AlgoritmoWilson.generar_laberinto(lab, matriz_laberinto, diccionario)
        return diccionario
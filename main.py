from Laberinto.Labyrinth import Labyrinth
from Gestion_Json.GestionJson import GestionJson
import Alg_Wilson.AlgoritmoWilson as AlgoritmoWilson
import Ventana.Ventana as Ventana
import pygame
import Cnfg
import sys
import os

def checkear_dirs():
    if not os.path.exists("JSONs"):
        os.mkdir("JSONs")

    if not os.path.exists("JPGs"):
        os.mkdir("JPGs")

def pedir_nombre_fichero():
    valido = False
    lab = None
    nombre_fichero = None
    while not valido:
        try:
            nombre_fichero = input("introduce el nombre del fichero con extensión .json:\n")
            lab = Labyrinth(nombre_fichero)
            valido = True
        except FileNotFoundError:
            print("\nNo se ha encontrado el archivo, vuelve a intentarlo\n")

    return lab, nombre_fichero

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

def menu_inicial():
    valido = False
    dict_manual = None
    lab = None
    while not valido:
        try:
            option = int(input(
                "Elige una opción [1,2]:\n\t1. Elegir archivo existente\n\t2. Generar algoritmo automáticamente\n\n"))
            if option == 1:
                lab, file_name = pedir_nombre_fichero()
                lab.load_data(None)
                dict_to_check = GestionJson.open_json_file(file_name)
                GestionJson.check_json(dict_to_check)
                valido = True
            elif option == 2:
                rows_cols = pedir_filas_columnas()
                lab = Labyrinth(None, rows_cols[0], rows_cols[1])
                lab.create_labyrinth()
                json = GestionJson(rows_cols[0], rows_cols[1])
                dict_manual = GestionJson.get_data(json)
                lab.load_data(dict_manual)
                dict_manual = AlgoritmoWilson.algoritmo_wilson(lab, dict_manual)
                lab.load_data(dict_manual)
                valido = True
            else:
                print("Intruduce un valor válido [1, 2]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2]\n")

    return [lab, dict_manual]

def main():
    checkear_dirs()
    lab, dict_data_manual = menu_inicial()
    screen = Ventana.inicializar_ventana(lab)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                name = "Laberinto_B1_2_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
                pygame.image.save(screen, "JPGs/{0}".format(name))
                sys.exit()

        screen.fill(Cnfg.WHITE)
        Ventana.dibujar(screen, lab)
        pygame.display.update()


if __name__ == '__main__':
    main()

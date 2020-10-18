from Laberinto.Labyrinth import Labyrinth
from Gestion_Json.GestionJson import GestionJson
from Alg_Wilson.AlgoritmoWilson import AlgoritmoWilson
from Ventana.Ventana import Ventana
from tkinter import filedialog
import tkinter as tk
import pygame
import Cnfg
import sys
import os

def pedir_filas():
    valido = False

    while not valido:
        try:
            row = int(input("\nIntroduce el número de filas: "))
            if row > 1:
                valido = True
            else:
                print("ERROR: Introduce un número de filas mayor que 1\n")
        except ValueError:
            print("ERROR: Introduce un caracter válido")

    return row


def pedir_colmnas():
    valido = False

    while not valido:
        try:
            cols = int(input("\nIntroduce el número de columnas: "))
            if cols > 1:
                valido = True
            else:
                print("ERROR: Introduce un número de columnas mayor que 1\n")
        except ValueError:
            print("ERROR: Introduce un caracter válido")

    return cols


def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    ruta = os.getcwd()
    file_name = filedialog.askopenfilename(initialdir=ruta, filetypes={("json files", "*.json")})
    try:
        lab = Labyrinth(file_name)

    except KeyError:
        print("Existen inconsistencias en la estructura del JSON")
        sys.exit()

    except FileNotFoundError:
        sys.exit()

    print(file_name)

    return lab, file_name

def menu_inicial():
    valido = False
    dict_manual = None
    lab = None
    while not valido:
        try:
            option = int(input(
                "Elige una opción [1,2]:\n\t1. Elegir archivo existente\n\t2. Generar algoritmo automáticamente\n\n"))
            if option == 1:
                lab, file_name = open_file_dialog()
                dict_to_check = GestionJson.leer_json(file_name)
                GestionJson.check_json(dict_to_check)
                lab.load_data(None)
                valido = True
            elif option == 2:
                rows = pedir_filas()
                cols = pedir_colmnas()
                lab = Labyrinth(None, rows, cols)
                lab.create_labyrinth()
                json = GestionJson(rows, cols)
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

def checkear_dirs():
    if not os.path.exists("JSONs"):
        os.mkdir("JSONs")

    if not os.path.exists("JPGs"):
        os.mkdir("JPGs")

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
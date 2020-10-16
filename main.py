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

def pedir_filas_columnas():
    valido = True
    valido2 = True
    row = None
    cols = None

    while valido:
        row = int(input("\nIntroduce el número de filas: "))
        if(row <= 1):
            print("ERROR: Introduce un número de filas mayor que 1\n")
        else:
            valido = False
    
    while valido2:
        cols = int(input("\nIntroduce el número de columnas: "))
        if(cols <= 1):
            print("ERROR: Introduce un número de columnas mayor que 1")
        else:
            valido2 = False

    return [row, cols]

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    ruta = os.getcwd()
    file_name = filedialog.askopenfilename(initialdir = ruta)
    try:
        lab = Labyrinth(file_name)
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
                lab.load_data(None)
                dict_to_check = GestionJson.leer_json(file_name)
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
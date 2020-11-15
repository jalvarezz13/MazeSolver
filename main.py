from Laberinto.Labyrinth import Labyrinth
from Laberinto.AlgoritmoWilson import AlgoritmoWilson

from Gestion_Json.LaberintoJson import LaberintoJson
from Gestion_Json.LeerProblemaJson import LeerProblemaJson
from Gestion_Json.CrearProblemaJson import CrearProblemaJson

from Problema.Nodo import Nodo
from Problema.Estado import Estado
from Problema.Frontera import Frontera

from Dibujar.Ventana import Ventana

from PIL import Image
from tkinter import filedialog
import tkinter as tk
import random
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


def open_file_dialog(leerProblema=None):
    root = tk.Tk()
    root.withdraw()
    root.call('wm', 'attributes', '.', '-topmost', True)
    ruta = os.getcwd()
    file_name = filedialog.askopenfilename(
        initialdir=ruta, filetypes={("json files", "*.json")})
    try:
        if leerProblema == None:
            try:
                lab = Labyrinth(file_name)
                print(file_name)
                return lab, file_name

            except KeyError:
                print("Existen inconsistencias en la estructura del JSON")
                sys.exit()
        else:
            print(file_name)
            if not file_name:
                sys.exit()
            return file_name

    except FileNotFoundError:
        sys.exit()


def elegirEstrategia():
    valido = False
    option = 0
    while not valido:
        try:
            option = int(input(
                "\nElige la estrategia [1,2,3,4,5]:\n\t1. Profundidad\n\t2. Anchura\n\t3. Voraz\n\t4. Costo uniforme\n\t5. A*\n\n"))
            if option >= 1 and option <= 5:
                valido = True
            else:
                print("Intruduce un valor válido [1, 2, 3, 4, 5]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2, 3, 4, 5]\n")

    return option


def menu_inicial():
    valido = False
    dict_manual = None
    lab = None
    file_name = None
    while not valido or option != 4:
        try:
            option = int(input(
                "\nElige una opción [1, 2, 3, 4]:\n\t1. Visualizar laberinto existente\n\t2. Generar laberinto con el algortimo Wilson \n\t3. Resolver problema\n\t4. Salir\n\n"))
            if option == 1:
                lab, file_name = open_file_dialog()
                dict_manual = LaberintoJson.leer_json(file_name)
                LaberintoJson.check_json(dict_manual)
                lab.load_data(None)
                valido = True
                guardarJpg(lab)
                if preguntarResolver():
                    elegirEstrategia()

            elif option == 2:
                rows = pedir_filas()
                cols = pedir_colmnas()
                lab = Labyrinth(None, rows, cols)
                lab.create_labyrinth()
                json = LaberintoJson(rows, cols)
                dict_manual = LaberintoJson.get_data(json)

                lab.load_data(dict_manual)
                dict_manual = AlgoritmoWilson.algoritmo_wilson(
                    lab, dict_manual)
                lab.load_data(dict_manual)
                valido = True
                guardarJpg(lab)
                if preguntarResolver():
                    elegirEstrategia()

            elif option == 3:
                file_name_problema = open_file_dialog(True)
                celda_inicial, celda_objetivo, file_name = LeerProblemaJson.getData(
                    file_name_problema)

                # lab = Labyrinth(file_name_problema)
                # dict_manual = LaberintoJson.leer_json(file_name)
                # LaberintoJson.check_json(dict_manual)
                # lab.load_data(None)

                elegirEstrategia()

                valido = True
                pass

            elif option==4:
                print("Programa finalizado")
                sys.exit()

            else:
                print("Intruduce un valor válido [1, 2, 3, 4]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2, 3, 4]\n")

    #Cnfg.objetivo = None
    return [lab, dict_manual, file_name]


def checkear_dirs():
    if not os.path.exists("Recursos"):
        os.mkdir("Recursos")

    if not os.path.exists("Recursos/JSONs"):
        os.mkdir("Recursos/JSONs")

    if not os.path.exists("Recursos/JPGs"):
        os.mkdir("Recursos/JPGs")

    if not os.path.exists("Recursos/SUCESORs"):
        os.mkdir("Recursos/SUCESORs")

    if not os.path.exists("Recursos/JSONs/PROBLEMAs"):
        os.mkdir("Recursos/JSONs/PROBLEMAs")


def generar_celda_random(lab):
    array = []
    array.append(random.randrange(0, lab.get_rows()))
    array.append(random.randrange(0, lab.get_cols()))
    return array


def preguntarResolver():
    valido = False
    while not valido:
        opcion = input("¿\nQuieres resolver el laberinto? (Y/n)\n")
        if opcion.lower() == "y" or opcion == "":
            valido == True
            return True
        elif opcion.lower() == "n":
            valido == True
            return False
        else:
            print("Introduce datos válidos (Y/n)")


def guardarJpg(lab):
    screen = Ventana.inicializar_ventana(lab)
    screen.fill(Cnfg.WHITE)
    Ventana.dibujar(screen, lab)
    pygame.display.update()

    name = "Laberinto_B1_2_" + \
        str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
    pygame.image.save(screen, "Recursos/JPGs/{0}".format(name))
    pygame.quit()

    img = Image.open(f"Recursos/JPGs/{name}")
    img.show()


def main():
    checkear_dirs()
    lab, dict_data_manual, name_fichero = menu_inicial()
   


    # lab, dict_data_manual, name_fichero = menu_inicial()
    # frontera1 = Frontera()

    # for i in range(5):
    #     celda = generar_celda_random(lab)
    #     estado = Estado(celda[0], celda[1])
    #     nodo = Nodo(0, 0, estado, None, 1, 1, 0)
    #     frontera1.insertar(nodo)
    #     nodo.generarSucesores(dict_data_manual, frontera1)

    # for nodo in frontera1.getFrontera():
    #     print(nodo.toString())


if __name__ == '__main__':
    main()
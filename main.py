from Laberinto.Labyrinth import Labyrinth
from Gestion_Json.GestionJson import GestionJson
from Gestion_Json.LeerProblema import LeerProblema
from Problema_Salir_Del_Laberinto.Nodo import Nodo
from Problema_Salir_Del_Laberinto.Estado import Estado
from Problema_Salir_Del_Laberinto.Frontera import Frontera
from Alg_Wilson.AlgoritmoWilson import AlgoritmoWilson
from Gestion_Json.ProblemaJson import ProblemaJson
from Ventana.Ventana import Ventana
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


def open_file_dialog(leerProblema = None):
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
            return file_name

    except FileNotFoundError:
        sys.exit()






def elegirEstrategia():
    valido = False
    option = 0
    while not valido:
        try:
            option = int(input(
                "Elige la estrategia [1,2,3,4,5]:\n\t1. Profundidad\n\t2. Anchura\n\t3. Voraz\n\t4. Costo uniforme\n\t5. A*\n\n"))
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
    while not valido:
        try:
            option = int(input(
                "Elige una opción [1,2,3]:\n\t1. Visualizar laberinto existente\n\t2. Generar laberinto con el algortimo Wilson \n\t3. Resolver problema\n\n"))
            if option == 1:
                lab, file_name = open_file_dialog()
                dict_manual = GestionJson.leer_json(file_name)
                GestionJson.check_json(dict_manual)
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
                dict_manual = AlgoritmoWilson.algoritmo_wilson(
                    lab, dict_manual)
                lab.load_data(dict_manual)
                valido = True
            elif option == 3:
                file_name_problema = open_file_dialog(True)
                celda_inicial, celda_objetivo, file_name = LeerProblema.getData(file_name_problema)



                # lab = Labyrinth(file_name_problema)
                # dict_manual = GestionJson.leer_json(file_name)
                # GestionJson.check_json(dict_manual)
                # lab.load_data(None)

                elegirEstrategia()

                valido = True
                pass
            else:
                print("Intruduce un valor válido [1, 2, 3]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2, 3]\n")

    return [option, lab, dict_manual, file_name]


def checkear_dirs():
    if not os.path.exists("JSONs"):
        os.mkdir("JSONs")

    if not os.path.exists("JPGs"):
        os.mkdir("JPGs")

    if not os.path.exists("SUCESORs"):
        os.mkdir("SUCESORs")

    if not os.path.exists("JSONs/PROBLEMAs"):
        os.mkdir("JSONs/PROBLEMAs")

def generar_celda_random(lab):
    array = []
    array.append(random.randrange(0, lab.get_rows()))
    array.append(random.randrange(0, lab.get_cols()))
    return array


def preguntarResolver():
    valido = False
    while not valido:
        opcion = input("¿Quieres resolver el laberinto? (si/no)")
        if opcion.lower() == "si":
            valido == True
            return True
        elif opcion.lower() == "no":
            valido == True
            return False
        else:
            print("Introduce datos válidos (si/no)")



def main():
    checkear_dirs()
    opcion, lab, dict_data_manual, name_fichero = menu_inicial()
    if opcion == 1 or opcion == 2:
        screen = Ventana.inicializar_ventana(lab)
        token = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    name = "Laberinto_B1_2_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
                    pygame.image.save(screen, "JPGs/{0}".format(name))
                    token = False
                    pygame.quit()
                    break

            if not token:
                break

            screen.fill(Cnfg.WHITE)
            Ventana.dibujar(screen, lab)
            pygame.display.update()

        if preguntarResolver():
            elegirEstrategia()

    # celda_inicio = generar_celda_random(lab)
    # celda_fin = generar_celda_random(lab)

    # if name_fichero is None:
    #     name_fichero = "Laberinto_Wilson_B1_2_{0}x{1}.json".format(dict_data_manual["rows"], dict_data_manual["cols"])
    # else:
    #     dir = name_fichero.split("/")
    #     name_fichero = dir[len(dir) - 1]
    # print("--------------------------")

    # ProblemaJson(celda_inicio, celda_fin, name_fichero)

    # for nombre_directorio, dirs, ficheros in os.walk(os.getcwd()):
    #     for nombre_fichero in ficheros:
    #         if nombre_fichero == name_fichero:
    #             print(nombre_fichero)

    frontera1 = Frontera()
    
    for i in range(5):
        celda = generar_celda_random(lab)
        estado = Estado(celda[0], celda[1])
        nodo = Nodo(0, 0, estado, None, 1, 1, 0)
        frontera1.insertar(nodo)
        nodo.generarSucesores(dict_data_manual, frontera1)

    for nodo in frontera1.getFrontera():
        print(nodo.toString())
    

if __name__ == '__main__':
    main()

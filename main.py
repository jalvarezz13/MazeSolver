from Laberinto.Labyrinth import Labyrinth
from Laberinto.AlgoritmoWilson import AlgoritmoWilson

from Gestion_Json.LaberintoJson import LaberintoJson
from Gestion_Json.LeerProblemaJson import LeerProblemaJson
from Gestion_Json.CrearProblemaJson import CrearProblemaJson

from Problema.Nodo import Nodo
from Problema.Estado import Estado
from Problema.Frontera import Frontera
from Problema.Busqueda import Busqueda

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
    row = None
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
    cols = None

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

    if leerProblema == None:
        ruta = os.getcwd() + "/Recursos/JSONs/MAZEs"

    elif leerProblema == True:
        ruta = os.getcwd() + "/Recursos/JSONs/PROBLEMAs"
        

    file_name = filedialog.askopenfilename(initialdir=ruta, filetypes={("json files", "*.json")})
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
    while not valido:
        try:
            option = int(input(
                "\nElige la estrategia [1, 2, 3, 4, 5]:\n\t1. Profundidad\n\t2. Anchura\n\t3. Voraz\n\t4. Costo "
                "uniforme\n\t5. A*\n\n"))
            if 1 <= option <= 5:
                valido = True
                Cnfg.estrategia = option
                if option == 1: Cnfg.estrategiaName = "DEPTH"
                elif option == 2: Cnfg.estrategiaName = "BREADTH"
                elif option == 3: Cnfg.estrategiaName = "GREEDY"
                elif option == 4: Cnfg.estrategiaName = "UNIFORM"
                else: Cnfg.estrategiaName = "A"
            else:
                print("Intruduce un valor válido [1, 2, 3, 4, 5]\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2, 3, 4, 5]\n")


def generar_problema(lab, dict_data_manual):
    celda_inicio = generar_celda_random(lab)
    celda_fin = generar_celda_random(lab)

    name_fichero = "Laberinto_Wilson_B1_2_{0}x{1}.json".format(dict_data_manual["rows"], dict_data_manual["cols"])
    print("--------------------------")
    print("Generando problema...")

    problema = CrearProblemaJson(celda_inicio, celda_fin, name_fichero)

    print("Problema generado: {0}".format(problema.get_nombre_problema()))

    return problema.get_nombre_problema(), problema.get_datos_problema()


def cargar_problema(option=None, nombre_problema=None):
    if option == 3:
        path_problema = open_file_dialog(True)
        dir = path_problema.split("/")
        nombre_problema = dir[len(dir) - 1]

    path = os.getcwd()+"\Recursos\JSONs\PROBLEMAs\{0}".format(nombre_problema)
    maze = LeerProblemaJson.getData(path)
    file_name = os.path.join("{0}/Recursos/JSONs/MAZEs/{1}".format(os.getcwd(), maze))

    lab = Labyrinth(file_name)
    dict_manual = LaberintoJson.leer_json(file_name)
    LaberintoJson.check_json(dict_manual)
    lab.load_data(dict_manual)

    print("----------------------------")

    return lab, dict_manual


def escoger_laberinto(token=None):
    lab, file_name = open_file_dialog()        
    dict = LaberintoJson.leer_json(file_name)
    LaberintoJson.check_json(dict)
    lab.load_data(None)
    return lab, dict


def inicializar_laberinto():
    rows = pedir_filas()
    cols = pedir_colmnas()

    lab = Labyrinth(None, rows, cols)
    lab.create_labyrinth()

    json = LaberintoJson(rows, cols)
    dict_manual = LaberintoJson.get_data(json)

    lab.load_data(dict_manual)

    return lab, dict_manual


def generar_laberinto_Wilson(lab, dict_manual):
    dict_manual = AlgoritmoWilson.algoritmo_wilson(lab, dict_manual)
    lab.load_data(dict_manual)

    guardarJpg(lab)

    return lab, dict_manual

def resolverProblema(nombre_problema=None, lab=None, diccionario=None):
    if nombre_problema is None:
        lab, diccionario = cargar_problema(option=3)

    elegirEstrategia()
    busqueda = Busqueda(diccionario)
    busqueda.algoritmoBusqueda()
    
    visitados = busqueda.getVisitados()
    frontera = busqueda.getFrontera()
    camino = busqueda.obtenerNodos()

    guardarJpg(lab, visitados=visitados, frontera=frontera, camino=camino)


def menu_inicial():
    valido = False
    option = None
    while not valido or option != 5:
        try:
            option = int(input(
                "\nElige una opción [1, 2, 3, 4, 5]:\n\t1. Visualizar laberinto existente\n\t2. Generar laberinto con el "
                "algortimo Wilson (y resolver) \n\t3. Resolver problema\n\t4. Crear problema con laberinto existente\n\t5. Salir\n\n"))

            if option == 1:
                lab,dict_manual=escoger_laberinto()
                guardarJpg(lab)
                valido = True

            elif option == 2:
                lab, dict_manual = inicializar_laberinto()
                lab, dict_manual = generar_laberinto_Wilson(lab, dict_manual)                

                if preguntarResolver():
                    nombre_problema, datos_problema = generar_problema(lab, dict_manual)
                    datos_problema.append(dict_manual)
                    resolverProblema(nombre_problema=nombre_problema, lab=lab, diccionario=dict_manual)

                valido = True

            elif option == 3:
                resolverProblema()
                valido = True
                pass

            elif option == 4:
                print("Seleccione el laberino sobre el cual quieres crear el problema.")
                lab, dict_manual=escoger_laberinto(True)
                nombre_problema, datos_problema = generar_problema(lab, dict_manual)
                
                if preguntarResolver():
                    datos_problema.append(dict_manual)
                    resolverProblema(nombre_problema=nombre_problema, lab=lab, diccionario=dict_manual)
                
                valido = True

            elif option == 5:
                print("Programa finalizado.")
                sys.exit()

            else:
                print("Intruduce un valor válido [1, 2, 3, 4]:\n")
        except ValueError:
            print("Intruduce un valor válido [1, 2, 3, 4]:\n")


def checkear_dirs():
    if not os.path.exists("Recursos"):
        os.mkdir("Recursos")

    # JPGs

    if not os.path.exists("Recursos/JPGs"):
        os.mkdir("Recursos/JPGs")

    if not os.path.exists("Recursos/JPGs/MAZEs"):
        os.mkdir("Recursos/JPGs/MAZEs")
    
    if not os.path.exists("Recursos/JPGs/SOLUTIONs"):
        os.mkdir("Recursos/JPGs/SOLUTIONs")

    # JSONs

    if not os.path.exists("Recursos/JSONs"):
        os.mkdir("Recursos/JSONs")

    if not os.path.exists("Recursos/JSONs/PROBLEMAs"):
        os.mkdir("Recursos/JSONs/PROBLEMAs")
    
    if not os.path.exists("Recursos/JSONs/MAZEs"):
        os.mkdir("Recursos/JSONs/MAZEs")
    
    # TXTs

    if not os.path.exists("Recursos/TXTs"):
        os.mkdir("Recursos/TXTs")

    if not os.path.exists("Recursos/TXTs/SOLUTIONs"):
        os.mkdir("Recursos/TXTs/SOLUTIONs")
    
    if not os.path.exists("Recursos/TXTs/SUCESORs"):
        os.mkdir("Recursos/TXTs/SUCESORs")

def generar_celda_random(lab):
    array = []
    array.append(random.randrange(0, lab.get_rows()))
    array.append(random.randrange(0, lab.get_cols()))
    return array


def preguntarResolver():
    valido = False
    while not valido:
        opcion = input("\n¿Quieres resolver el laberinto? (Y/n)\n")
        if opcion.lower() == "y" or opcion == "":
            valido == True
            return True
        elif opcion.lower() == "n":
            valido == True
            return False
        else:
            print("Introduce datos válidos (Y/n)")


def guardarJpg(lab, visitados=None, frontera=None, camino=None):
    screen = Ventana.inicializar_ventana(lab)
    screen.fill(Cnfg.WHITE)

    if camino is not None:
        name = "SOLUCION_Laberinto_B1_2_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + "_" + str(Cnfg.estrategiaName) + "_.jpg"
        Ventana.dibujarSol(screen, lab, visitados, frontera, camino)
        pygame.display.update()
        pygame.image.save(screen, "Recursos/JPGs/SOLUTIONs/{0}".format(name))
        pygame.quit()
        img = Image.open(f"Recursos/JPGs/SOLUTIONs/{name}")
    else:
        name = "Laberinto_B1_2_" + str(lab.get_rows()) + "x" + str(lab.get_cols()) + ".jpg"
        Ventana.dibujar(screen, lab)
        pygame.display.update()
        pygame.image.save(screen, "Recursos/JPGs/MAZEs/{0}".format(name))
        pygame.quit()
        img = Image.open(f"Recursos/JPGs/MAZEs/{name}")

    img.show()


def main():
    checkear_dirs()
    menu_inicial()


if __name__ == '__main__':
    main()

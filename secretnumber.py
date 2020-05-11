
from prettytable import from_csv, PrettyTable
import random
import datetime


class Resultado():
    def __init__(self, puntuacion, nombre_jugador, fecha):
        self.puntuacion = puntuacion
        self.nombre_jugador = nombre_jugador
        self.fecha = fecha


table = PrettyTable(["puntuacion", "Nombre_Jugador", "Fecha"])


def jugar():

    usuario = input("Introduce tu nombre de usuario: ")
    secret = random.randint(1, 30)
    intentos = 0

    while True:
        num_usuario = int(input("Introduzca el numero secreto (Entre 1 y 30)"))
        intentos += 1

        if num_usuario == secret:

            jugador = Resultado(puntuacion=intentos,nombre_jugador=usuario,fecha=str(datetime.datetime.now()))

            with open("results.csv", "a") as results_file:
                results_file.write(str(jugador.__dict__))

            print("\nEnhorabuena acertaste el numero secreto: " + str(secret))

            # print("\nDatos del jugador en la partida: ", jugador.__dict__)

            table.add_row([jugador.puntuacion, jugador.nombre_jugador, jugador.fecha + "\n"])

            break

        elif num_usuario > secret:
            print("El numero introducido no es correcto... Prueba con un numero mas pequeño")

        elif num_usuario < secret:
            print("El numero introducido no es correcto... Prueba con un numero mas grande")


while True:
    print("""
    [1].- Jugar a Adivina el numero secreto --->
    [2].- Mostrar partidas de la sesion actual --->
    [3].- Mostrar registro de todas las puntuaciones --->
    [4].- Salir del juego --->
    """)

    opcion = input("Seleccione la opcion para empezar: ")

    if opcion == "1":
        jugar()

    elif opcion == "2":
        print("PARTIDAS SESION ACTUAL:")
        print(table)

    elif opcion == "3":
        print("REGISTRO GENERAL DE PUNTUACIONES GUARDADAS")
        with open("results.csv", "r") as results_file:
            x = from_csv(results_file)
        print (x)

    elif opcion == "4":
        print("Saliendo de la aplicacion....")

        break

    else:
        print("OPCION INCORRECTA! INTRODUZCA LA OPCION CORRESPONDIENTE (1-4)")
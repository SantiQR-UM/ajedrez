from tablero import Tablero

def main():
    tablero = Tablero()
    
    while True:
        print("\n¿Qué desea hacer?\n")
        print("1. Iniciar el juego")
        print("2. Cerrar")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print()
            tablero.imprimir_tablero()
            print()

            while True:
                print("1. Mover pieza")
                print("2. Finalizar juego (Empate)")
                accion = input("\nSeleccione una opción: ")

                if accion == "1":
                    # Lógica para mover piezas
                    pass

                elif accion == "2":
                    print("\nJuego finalizado en empate.\n")
                    exit()

        elif opcion == "2":
            print("\nCerrando el juego.\n")
            break

        else: 
            print("\nOpción no válida.\n")
            continue

if __name__ == "__main__":
    main()

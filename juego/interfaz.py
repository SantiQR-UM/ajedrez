from juego.ajedrez import *

def main():
    juego = Ajedrez()
    
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Iniciar el juego")
        print("2. Cerrar")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            iniciar_juego(juego)

        elif opcion == "2":
            print("\nCerrando el juego.\n")
            exit()

        else: 
            print("\nOpción no válida.\n")
            continue


def iniciar_juego(juego):
    while True:
        imprimir_tablero(juego)

        print("\n1. Mover pieza (" + juego.__turno__ + "s mueven)")
        print("2. Finalizar juego (Empate)")
        accion = input("\nSeleccione una opción: ")

        if accion == "1":
            # Empezamos el juego
            juego = Ajedrez.jugar(juego)

            opciones_1(juego)
            
            # Verifico resultado de la partida
            juego.__tablero__.verificar_victoria()

            # Cambio el color si ya movio
            juego.cambiar_turno()

        elif accion == "2":
            print("\nJuego finalizado en empate.\n")
            break
        
        else: 
            print("\nOpción no válida.\n")
            continue


def opciones_1(juego):
    
    # Hago un print del tablero para mostrarlo antes de dar opciones.
    while True:    
        
        imprimir_tablero(juego)

        # Muestro los nombres de las piezas que se pueden mover, no las instancias.
        print("\nOpciones:")
        
        k = 1
        for pieza in juego.__lista_piezas__:
            print(f"{k}. {pieza}")
            k += 1
        
        opcion = input("\nSeleccione una opción: ")
        
        # Pido la opción, si falla, vuelve al bucle.
        opcion, isOK = chequear_opcion(opcion, k-1)
        if not isOK:
            continue

        resultado = opciones_2(juego, opcion)
        if resultado:
            return


def opciones_2(juego, opcion):
        
    imprimir_tablero(juego)

    # Muestro las instancias de la pieza que elegí, ¡solo las que se pueden mover!
    print("\nInstancias de la pieza:")

    count = 1
    elegir = [] # Uso esta lista para guardar los índices de la lista de instancias que se 
            # pueden mover para luego cuando la elija pueda usar esta lista y referenciarla.
    for z in range(len(juego.__lista_instancias__)):
        
        # lista_piezas[opcion-1] es el nombre de la pieza elegida.
        # lista_instancias[z].__nom__ es el nombre de la instancia de la pieza.
        if juego.__lista_piezas__[opcion-1] == juego.__lista_instancias__[z].__nom__:
            
            # Convierto las coordenadas de la pieza a la notación de la tabla.
            x, y = conversion_coordenadas(juego.__lista_instancias__[z].__posicion__) # (Función cerca del final).

            # Muestro las opciones.
            print(f"{count}. {juego.__lista_instancias__[z].__nom__} {x}{y}")
            elegir.append(z)
            count += 1
    print(f"{count}. Atrás") # Opción extra para volver atrás.

    # Para depurar:
    # print("count: ",count)

    # Pido la opción de la instancia, si falla, vuelve al bucle.
    opcion_2 = input("\nSeleccione una pieza: ") # Para elegir una pieza o salir

    opcion_2, isOK = chequear_opcion(opcion_2, count)
    if not isOK:
        return False
    
    if opcion_2 == count:
        return False  # Salir para volver a preguntar por la pieza.

    else: 
        # Elijo mover una pieza:
        # Obtengo el índice de la instancia de la pieza de la lista elegir.
        nro_instancia = elegir[opcion_2-1] 
        # Obtengo las posibilidades de esa instancia.
        posibilidades_finales = juego.__lista_posibilidades__[nro_instancia] 
        # Uso el método 'search' para buscarla (también uso el metodo var() de la pieza).
        seleccion = juego.__tablero__.__BD_piezas__.search(juego.__lista_instancias__[nro_instancia].var())
        
        # Pido la nueva posición.
        nueva_posicion = input("Ingrese la nueva posición (ej. 'a3'): ") 
        
        # Muevo la pieza.                
        resultado = mover(juego, seleccion, nueva_posicion, posibilidades_finales)
        if resultado:
            return True # Si se completa el movimiento, salgo del bucle.
                
                
def mover(juego, seleccion, nueva_posicion_str, posibilidades_finales):
    
    posicion = conversion_coordenadas_inversa(nueva_posicion_str)
    if not posicion:
        return False
    nueva_posicion_int = posicion

    # Convierto las coordenadas de la pieza a la notación de la tabla para mostrar en pantalla.
    posicion = conversion_coordenadas(seleccion.__posicion__)
    if not posicion:
        return False
    vieja_posicion = posicion

    # Verifico si la nueva posición está dentro de las posibilidades
    if nueva_posicion_int not in posibilidades_finales:
        print("\nEste movimiento no es posible.\n")
        return False
    
    juego, movimiento = juego.mover_ajedrez(seleccion, nueva_posicion_str, \
                        nueva_posicion_int, vieja_posicion, posibilidades_finales)

    if movimiento:
        return True


def imprimir_tablero(juego):
    juego.imprimir_tablero_ajedrez()


def chequear_opcion(opcion, k):
    try:
        opcion = int(opcion)
        
        if opcion > k or opcion == 0:
            print("\nOpción no válida.\n")
            return False
    
        return opcion, True

    except ValueError:
        print("\nOpción no válida.\n")
        return opcion, False
    

def conversion_coordenadas(posicion):
    # Convierto las coordenadas de la pieza a la notación de la tabla.

    columnas = {1 :'a', 2 :'b', 3 :'c', 4 :'d', 5 :'e', 6 :'f', 7 :'g', 8 :'h'}
    filas = {8 :'1', 7 :'2', 6 :'3', 5 :'4', 4 :'5', 3 :'6', 2 :'7', 1 :'8'}
    try:
        nueva_columna, nueva_fila = posicion

        x = columnas[nueva_columna]
        y = filas[nueva_fila]

    except (KeyError, ValueError, TypeError, IndexError):
        print("\nValores mal ingresados.\n")
        return False

    return x, y # Devuelvo las coordenadas convertidas.


def conversion_coordenadas_inversa(posicion):
    # Convierto la notación de la tabla a las coordenadas de la pieza.

    columnas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    filas = {'1': 8, '2': 7, '3': 6, '4': 5, '5': 4, '6': 3, '7': 2, '8': 1}
    
    try:
        nueva_columna, nueva_fila = posicion[0], posicion[1]
        
        x = columnas[nueva_columna]
        y = filas[nueva_fila]

    except (KeyError, ValueError, TypeError, IndexError):
        print("\nValores mal ingresados.\n")
        return False

    return x, y # Devuelvo las coordenadas convertidas.


if __name__ == "__main__":
    main()

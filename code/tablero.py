from piezas import Peon, Caballo, Alfil, Dama, Rey, Torre, Pieza, Casilla

class Tablero:
    def __init__(self):
        self.tablero = self.crear_tablero_inicial()

    def crear_tablero_inicial(self):
        # Creamos las piezas y los espacios:

        # Piezas blancas
        P1 = Peon(color="blanca", posicion=('a',2), s=u"\u2659", color_casilla="negra") # ♙
        P2 = Peon(color="blanca", posicion=('b',2), s=u"\u2659", color_casilla="blanca") # ♙
        P3 = Peon(color="blanca", posicion=('c',2), s=u"\u2659", color_casilla="negra") # ♙
        P4 = Peon(color="blanca", posicion=('d',2), s=u"\u2659", color_casilla="blanca") # ♙
        P5 = Peon(color="blanca", posicion=('e',2), s=u"\u2659", color_casilla="negra") # ♙
        P6 = Peon(color="blanca", posicion=('f',2), s=u"\u2659", color_casilla="blanca") # ♙
        P7 = Peon(color="blanca", posicion=('g',2), s=u"\u2659", color_casilla="negra") # ♙
        P8 = Peon(color="blanca", posicion=('h',2), s=u"\u2659", color_casilla="blanca") # ♙
        C1 = Caballo(color="blanca", posicion=('b',1), s=u"\u2658", color_casilla="blanca") # ♘
        C2 = Caballo(color="blanca", posicion=('g',1), s=u"\u2658", color_casilla="negra") # ♘
        A1 = Alfil(color="blanca", posicion=('c',1), s=u"\u2657", color_casilla="negra") # ♗
        A2 = Alfil(color="blanca", posicion=('f',1), s=u"\u2657", color_casilla="blanca") # ♗
        T1 = Torre(color="blanca", posicion=('a',1), s=u"\u2656", color_casilla="negra") # ♖
        T2 = Torre(color="blanca", posicion=('h',1), s=u"\u2656", color_casilla="blanca") # ♖
        D = Dama(color="blanca", posicion=('d',5), s=u"\u2655", color_casilla="blanca") # ♕
        R = Rey(color="blanca", posicion=('e',6), s=u"\u2654", color_casilla="negra") # ♔
        
        # Piezas negras
        p1 = Peon(color="negra", posicion=('a',7), s=u"\u265F", color_casilla="negra") # ♟
        p2 = Peon(color="negra", posicion=('b',7), s=u"\u265F", color_casilla="blanca") # ♟
        p3 = Peon(color="negra", posicion=('c',7), s=u"\u265F", color_casilla="negra") # ♟
        p4 = Peon(color="negra", posicion=('d',7), s=u"\u265F", color_casilla="blanca") # ♟
        p5 = Peon(color="negra", posicion=('e',7), s=u"\u265F", color_casilla="negra") # ♟
        p6 = Peon(color="negra", posicion=('f',7), s=u"\u265F", color_casilla="blanca") # ♟
        p7 = Peon(color="negra", posicion=('g',7), s=u"\u265F", color_casilla="negra") # ♟
        p8 = Peon(color="negra", posicion=('h',7), s=u"\u265F", color_casilla="blanca") # ♟
        c1 = Caballo(color="negra", posicion=('b',8), s=u"\u265E", color_casilla="negra") # ♞
        c2 = Caballo(color="negra", posicion=('g',8), s=u"\u265E", color_casilla="blanca") # ♞
        a1 = Alfil(color="negra", posicion=('c',8), s=u"\u265D", color_casilla="blanca") # ♝
        a2 = Alfil(color="negra", posicion=('f',8), s=u"\u265D", color_casilla="negra") # ♝
        t1 = Torre(color="negra", posicion=('a',8), s=u"\u265C", color_casilla="blanca") # ♜
        t2 = Torre(color="negra", posicion=('h',8), s=u"\u265C", color_casilla="negra") # ♜
        d = Dama(color="negra", posicion=('d',8), s=u"\u265B", color_casilla="negra") # ♛
        r = Rey(color="negra", posicion=('e',8), s=u"\u265A", color_casilla="blanca") # ♚

        # Espacios
        B = Casilla(color="blanca", s=u"\u25A1")  # Espacio blanco □
        N = Casilla(color="negra", s=u"\u25A0")  # Espacio negro ■

        # Crear y colocar las piezas en su posición inicial usando objetos de las clases:
        
        tablero = [
        [t1.s, c1.s, a1.s, d.s, r.s, a2.s, c2.s, t2.s],
        [p1.s, p2.s, p3.s, p4.s, p5.s, p6.s, p7.s, p8.s],
        [B.s, N.s, B.s, N.s, B.s, N.s, B.s, N.s],
        [N.s, B.s, N.s, B.s, N.s, B.s, N.s, B.s],
        [B.s, N.s, B.s, N.s, B.s, N.s, B.s, N.s],
        [N.s, B.s, N.s, B.s, N.s, B.s, N.s, B.s],
        [P1.s, P2.s, P3.s, P4.s, P5.s, P6.s, P7.s, P8.s],
        [T1.s, C1.s, A1.s, D.s, R.s, A2.s, C2.s, T2.s]
        ]
        
        return tablero

    def imprimir_tablero(self):
        for fila in self.tablero:
            for casilla in fila:
                print(casilla.s if isinstance(casilla, Pieza) else casilla, end=' ')
            print()

    def mover_pieza(self, pieza, nueva_posicion):
        # Logica para mover una pieza en el tablero
        pass

    def obtener_piezas_movibles(self, color):
        # Devuelve una lista de piezas que pueden moverse para el color dado
        pass

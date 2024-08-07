class Casilla:
    def __init__(self, color, s):
        self.color = color
        self.s = s

class Pieza:
    def __init__(self, color, posicion, s, color_casilla):
        self.color = color
        self.posicion = posicion
        self.s = s
        self.color_casilla = color_casilla

    def movimientos_posibles(self, tablero):
        # Este método debe ser implementado por cada pieza específica
        pass

    def mover(self, nueva_posicion):
    # Actualiza la posición de la pieza
        self.posicion = nueva_posicion


class Peon(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos del peón
        pass


class Caballo(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos del caballo
        pass

class Torre(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos de la torre
        pass

class Alfil(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos del alfil
        pass

class Dama(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos de la dama
        pass

class Rey(Pieza):
    def movimientos_posibles(self, tablero):
        # Lógica para los movimientos del rey
        pass
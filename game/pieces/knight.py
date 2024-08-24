from game.pieces.pieces import Piece

class Knight(Piece):
    def __init__(self, id, color, position, name):
        super().__init__(id, color, position, name)

    # To return the symbol of the box.
    def __str__(self):
        if self.__color__ == "white":
            return u"\u2658"
        else:
            return u"\u265E"
        
    # Función especializada para el caballo.
    def possible_movements(self):
        movements = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        limit = True
        return self.calculate_movements(self.__position__, movements, limit)
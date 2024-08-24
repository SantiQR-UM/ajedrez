from game.pieces.pieces import Piece

class King(Piece):
    def __init__(self, id, color, position, name):
        super().__init__(id, color, position, name)

    # To return the symbol of the box.
    def __str__(self):
        if self.__color__ == "white":
            return u"\u2654"
        else:
            return u"\u265A"
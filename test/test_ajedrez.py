import unittest
from unittest.mock import MagicMock
from juego.tablero import Tablero
from juego.ajedrez import Ajedrez
import sys
from io import StringIO

class TestAjedrez(unittest.TestCase):
    def setUp(self):
        self.ajedrez = Ajedrez()

    def test_cambiar_turno(self):
        self.assertEqual(self.ajedrez.__turno__, "blanca")
        self.ajedrez.cambiar_turno()
        self.assertEqual(self.ajedrez.__turno__, "negra")
        self.ajedrez.cambiar_turno()
        self.assertEqual(self.ajedrez.__turno__, "blanca")

    def test_jugar(self):
        self.ajedrez.jugar()
        self.assertIsNotNone(self.ajedrez.__lista_piezas__)
        self.assertIsNotNone(self.ajedrez.__lista_instancias__)
        self.assertIsNotNone(self.ajedrez.__lista_posibilidades__)

    def test_imprimir_tablero_ajedrez(self):
        # Redirect stdout to capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        self.ajedrez.imprimir_tablero_ajedrez()

        sys.stdout = sys.__stdout__
        assert '''  a b c d e f g h   
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7 
6 □ ■ □ ■ □ ■ □ ■ 6 
5 ■ □ ■ □ ■ □ ■ □ 5 
4 □ ■ □ ■ □ ■ □ ■ 4 
3 ■ □ ■ □ ■ □ ■ □ 3 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1 
  a b c d e f g h   ''' in captured_output.getvalue()  # Es medio feo, pero funciona jajaja.

    def test_mover_ajedrez(self):
        seleccion = MagicMock()
        seleccion.__nom__ = "Peon"
        seleccion.__color__ = "negra"
        seleccion.__posicion__ = (2, 2)
        nueva_posicion_str = "b5"
        nueva_posicion_int = (2, 4)
        vieja_posicion = ('b', '7')
        posibilidades_finales = [(2, 3), (2, 4)]

        ajedrez, string_movimiento = \
            self.ajedrez.mover_ajedrez(seleccion, nueva_posicion_str,
                                        nueva_posicion_int, vieja_posicion,
                                        posibilidades_finales)

        self.assertEqual(string_movimiento, "\nMovimiento realizado: Peon negra b7 se ha movido a b5\n")

    def test_verificar_fin(self):
        self.ajedrez.__tablero__ = Tablero()
        self.assertFalse(self.ajedrez.verificar_fin())

if __name__ == '__main__':
    unittest.main()
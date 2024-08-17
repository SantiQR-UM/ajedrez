import unittest
from unittest.mock import patch, MagicMock
from juego.interfaz import *
from juego.ajedrez import *

class TestInterfaz(unittest.TestCase):

    def setUp(self):
        self.__juego__ = Juego()

    @patch('builtins.input', side_effect=['1', '1', '1', '1', 'a3', '2', '2'])
    @patch('builtins.print') 
    @patch('sys.exit')
    def test_main_juego_movimiento(self, mock_exit, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            self.__juego__.main()
        self.assertEqual(mock_input.call_count, 7)
        mock_print.assert_any_call("\nJuego finalizado en empate.\n")
    

    @patch('builtins.input', side_effect=['1', '1', '1', 'a3'])
    @patch('builtins.print') 
    def test_iniciar_juego_victoria(self, mock_print, mock_input):
        
        self.__juego__.__ajedrez__.verificar_fin = MagicMock(return_value="victoria")
        self.__juego__.iniciar_juego()
            
        self.assertEqual(mock_input.call_count, 4)
        mock_print.assert_any_call("victoria")


    @patch('builtins.input', side_effect=['1', '3', '2', '2'])
    @patch('builtins.print') 
    @patch('sys.exit')
    def test_main_juego_salir(self, mock_exit, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            self.__juego__.main()
        self.assertEqual(mock_input.call_count, 4)
        mock_print.assert_any_call("\nOpción no válida.\n")
        mock_print.assert_any_call("\nJuego finalizado en empate.\n")

    @patch('builtins.input', side_effect=['3', '2'])
    @patch('builtins.print')
    @patch('sys.exit')
    def test_cerrar_juego(self, mock_exit, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            self.__juego__.main()
        self.assertEqual(mock_input.call_count, 2)
        mock_print.assert_any_call("\nOpción no válida.\n")
        mock_print.assert_any_call("\nCerrando el juego.\n")

    @patch('builtins.input', side_effect=['1', '9', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_2_atras_y_blancas(self, mock_print, mock_input):

        self.__juego__.__ajedrez__ = Ajedrez.jugar(self.__juego__.__ajedrez__)
        resultado = self.__juego__.opciones_1()

        self.assertIsNone(resultado)
        self.assertEqual(mock_input.call_count, 5)

    @patch('builtins.input', side_effect=['a', '0', '1', 'a', '1', '0', '1', '1', '', '1', '1', 'a3'])
    @patch('builtins.print')
    def test_main_2_errores(self, mock_print, mock_input):

        self.__juego__.__ajedrez__ = Ajedrez.jugar(self.__juego__.__ajedrez__)
        resultado = self.__juego__.opciones_1()

        self.assertIsNone(resultado)
        self.assertEqual(mock_input.call_count, 12)
        count = 0
        for call in mock_print.call_args_list:
            args, _ = call
            if len(args) > 0 and args[0] == "\nOpción no válida.\n":
                count += 1
        self.assertEqual(count, 4)

    @patch('builtins.input', side_effect=['1', '1', 'a3'])
    @patch('builtins.print')
    def test_opciones_1(self, mock_print, mock_input):

        self.__juego__.__ajedrez__ = Ajedrez.jugar(self.__juego__.__ajedrez__)
        resultado = self.__juego__.opciones_1()

        self.assertIsNone(resultado)
        self.assertEqual(mock_input.call_count, 3)

    @patch('builtins.input', side_effect=['1', '1'])
    @patch('builtins.print')
    def test_opciones_2(self, mock_print, mock_input):

        self.__juego__.__ajedrez__ = Ajedrez.jugar(self.__juego__.__ajedrez__)
        resultado = self.__juego__.opciones_2(1)

        self.assertFalse(resultado)

    @patch('builtins.input', side_effect=['1', '1', 'a3'])
    @patch('builtins.print')
    def test_mover(self, mock_print,  mock_input):

        seleccion = MagicMock(spec = Peon)
        seleccion.__posicion__ = (1, 7)
        seleccion.__nom__ = 'Peon'
        seleccion.__color__ = 'blanca'
        posibilidades_finales = [(1, 6)]
        resultado = self.__juego__.mover(seleccion, 'a3', posibilidades_finales)

        self.assertTrue(resultado)

    @patch('builtins.input', side_effect=['1', '1', 'a6'])
    @patch('builtins.print')
    def test_mover_errores(self, mock_print,  mock_input):

        seleccion = MagicMock(spec = Peon)
        seleccion.__posicion__ = (1, 7)
        seleccion.__nom__ = 'Peon'
        seleccion.__color__ = 'blanca'
        posibilidades_finales = [(1, 6)]

        seleccion_error = MagicMock(spec = Peon)
        seleccion_error.__posicion__ = (1)
        seleccion_error.__nom__ = 'Peon'
        seleccion_error.__color__ = 'blanca'
        posibilidades_finales_error = [(1, 6)]
        
        resultado = self.__juego__.mover(seleccion, 'a6', posibilidades_finales)
        self.assertFalse(resultado)

        resultado = self.__juego__.mover(seleccion, 'a', posibilidades_finales)
        self.assertFalse(resultado)

        resultado = self.__juego__.mover(seleccion_error, 'a6', posibilidades_finales_error)
        self.assertFalse(resultado)

    # Testeo que conversion_coordenadas funciona.
    @patch('builtins.print')
    def test_conversion_coordenadas(self, mock_print):
        x, y = InterfazDeUsuario.conversion_coordenadas((1, 8))
        self.assertEqual((x, y), ('a', '1'))

    # Testeo que conversion_coordenadas funciona.
    @patch('builtins.print')
    def test_conversion_coordenadas_inversa(self, mock_print):
        x, y = InterfazDeUsuario.conversion_coordenadas_inversa("a1")
        self.assertEqual((x, y), (1, 8))

if __name__ == '__main__':
    unittest.main()

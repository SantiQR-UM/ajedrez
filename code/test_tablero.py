import unittest
from unittest.mock import patch, MagicMock
from tablero import Tablero
from piezas import Pieza, Espacio, Peon, Torre, Caballo
from BD import BD
import io
import sys

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.__tablero__ = Tablero()
        self.__BD_piezas__ = BD()
        self.__BD_espacios__ = BD()

    def test_crear_tablero_inicial(self):
        self.assertIsInstance(self.__tablero__.__tablero__, list)
        # Verificar que son instancias de BD
        self.assertIsInstance(self.__tablero__.__BD_piezas__, BD)  
        self.assertIsInstance(self.__tablero__.__BD_espacios__, BD)  


    def test_imprimir_tablero(self):
        tablero = Tablero()
        captured_output = io.StringIO()  # Crear un buffer en memoria
        sys.stdout = captured_output  # Redirigir stdout al buffer
        tablero.imprimir_tablero()  # Llamar al método
        sys.stdout = sys.__stdout__  # Restaurar stdout
        assert '''  a b c d e f g h   
8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ 8 
7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ 7 
6 □ ■ □ ■ □ ■ □ ■ 6 
5 ■ □ ■ □ ■ □ ■ □ 5 
4 □ ■ □ ■ □ ■ □ ■ 4 
3 ■ □ ■ □ ■ □ ■ □ 3 
2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ 2 
1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 1 
  a b c d e f g h   ''' in captured_output.getvalue()  # Verificar contenido

    @patch('builtins.input', side_effect=['1', '1', 'a6'])  # Simular entrada del usuario
    @patch('builtins.print')
    def test_obtener_piezas_movibles_negras(self, mock_print, mock_input):
        # Configurar piezas negras en la BD con MagicMock y simular que algunas se pueden mover
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "p"
        pieza_mock.__posicion__ = (1, 2)
        pieza_mock.var.return_value = "p1"
        self.__BD_piezas__.add(pieza_mock)
        
        # Seteo a que instancias_piezas solo pueda devolver pieza_mock y True
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(1, 3)]))  # Simulando que el peón puede moverse a 'a3'
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  # Simular el movimiento de la pieza

        result = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "negra")
        
        # Verificar que la pieza fue seleccionada y se intentó mover
        self.assertIsNone(result) # Verificar que vuelvo a interfaz con return None
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'a6', [(1, 3)]) # Verificar que se ha llamado a mover_pieza con la pieza y la posición correcta

    @patch('builtins.input', side_effect=['1', '1', 'g3'])
    @patch('builtins.print')
    def test_obtener_piezas_movibles_blancas(self, mock_print, mock_input):
        # Configurar piezas blancas en la BD con MagicMock y simular que algunas se pueden mover
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "P"
        pieza_mock.__posicion__ = (7, 7)
        pieza_mock.var.return_value = "P7"
        self.__BD_piezas__.add(pieza_mock)
        
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(7, 6)]))  # Simulando que el peón puede moverse a 'a6'
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  # Simular el movimiento de la pieza

        result = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")
        
        # Verificar que la pieza fue seleccionada y se intentó mover
        self.assertIsNone(result)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'g3', [(7, 6)])

    @patch('builtins.input', side_effect=['1', '2', '1', '1', 'a3'])  # Simulando entrada del usuario para elegir atrás
    @patch('builtins.print')  # Mock de print para evitar la salida en los tests
    def test_obtener_piezas_movibles_atras_y_blancas(self, mock_print, mock_input):
        # Configurar piezas y simular el escenario donde el usuario selecciona "Atrás"
        pieza_mock = MagicMock()
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__posicion__ = (1, 7)
        pieza_mock.var.return_value = "P1"
        self.__BD_piezas__.add(pieza_mock)
        
        self.__tablero__.instancias_piezas = MagicMock(return_value=(pieza_mock, True, [(1, 6)]))  # Simulando que el peón puede moverse a 'a6'
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  # Simular el movimiento de la pieza

        result = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")

        # Verificar que la pieza fue seleccionada y se intentó mover
        self.assertIsNone(result)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock, 'a3', [(1, 6)])
        self.assertEqual(mock_input.call_count, 5)

    @patch('builtins.input', side_effect=['a', '0', '1', 'a', '1', '0', '1', '1', '', '1', '1', 'a3'])  # Simulando entrada del usuario para los errores
    @patch('builtins.print')  # Mock de print para evitar la salida en los tests
    def test_obtener_piezas_movibles_errores(self, mock_print, mock_input):
        # Configurar piezas y simular el escenario donde movible == False
        pieza_mock_1 = MagicMock()
        pieza_mock_1.__nom__ = "Peon"
        pieza_mock_1.__posicion__ = (1, 7)
        pieza_mock_1.var.return_value = "P1"
        self.__BD_piezas__.add(pieza_mock_1)

        pieza_mock_2 = MagicMock()
        pieza_mock_2.__nom__ = "Peon"
        pieza_mock_2.__posicion__ = (2, 7)
        pieza_mock_2.var.return_value = "P2"
        self.__BD_piezas__.add(pieza_mock_2)
        
        # Usar side_effect para alternar entre los dos retornos esperados
        # Crear la secuencia deseada: False una vez y True 15 veces
        secuencia = [(pieza_mock_2, False, [])] + [(pieza_mock_1, True, [(1, 6)])] * 15

        # Repetir la secuencia
        resultados = secuencia * 6
        
        self.__tablero__.instancias_piezas = MagicMock(side_effect=resultados)
        
        self.__tablero__.mover_pieza = MagicMock(return_value=True)  # Simular el movimiento de la pieza

        result = self.__tablero__.obtener_piezas_movibles(self.__BD_piezas__, "blanca")

        # Verificar que la pieza fue seleccionada y se intentó mover
        self.assertIsNone(result)
        self.__tablero__.mover_pieza.assert_called_once_with(pieza_mock_1, 'a3', [(1, 6)])
        self.assertEqual(mock_input.call_count, 12)
        
        count = 0
        for call in mock_print.call_args_list:
            args, _ = call
            if len(args) > 0 and args[0] == "\nOpción no válida.\n":
                count += 1
        self.assertEqual(count, 5)

    def test_instancias_piezas(self):
        pieza, movible, posibilidades = self.__tablero__.instancias_piezas(self.__tablero__.__BD_piezas__, 'P', 1)
        self.assertIsInstance(pieza, Peon)

    def test_movible_peon_vertical(self):
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movible, posibilidades = self.__tablero__.movible(pieza)
        self.assertTrue(movible)

    def test_movible_peon_diagonal(self):
        # Mockear una instancia de Peon
        pieza_peon = MagicMock(spec=Peon)
        pieza_peon.__nom__ = "Peon"
        pieza_peon.__color__ = "negra"
        pieza_peon.__posicion__ = (3, 3)
        pieza_peon.__vive__ = True

        # Simular la posibilidad de movimientos del peón (diagonales)
        pieza_peon.movimientos_posibles.return_value = [(2, 4), (4, 4)]

        # Crear un mock del tablero, con casillas y piezas
        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]
        
        # Configurar casillas específicas para que devuelvan instancias de Pieza enemiga
        # Tengo que pasarlo como [y][x] porque el mock de tablero es un array de array
        # Estuve 2 horas como boludo hasta que me di cuenta jajajaja
        self.__tablero__.__tablero__[4][2] = MagicMock(spec=Pieza, __color__="blanca")
        self.__tablero__.__tablero__[4][4] = MagicMock(spec=Pieza, __color__="blanca")

        # Llamar al método 'movible' de 'tablero'
        movible, posibilidades = self.__tablero__.movible(pieza_peon)

        # Verificar que el peón puede moverse en diagonal
        self.assertIn((2, 4), posibilidades)
        self.assertIn((4, 4), posibilidades)
        self.assertTrue(movible)


    def test_movible_caballo(self):
        # Crear una pieza caballo con una posición en (4, 4)
        pieza_caballo = MagicMock(spec=Caballo)
        pieza_caballo.__nom__ = "Caballo"
        pieza_caballo.__color__ = "blanco"
        pieza_caballo.__posicion__ = (4, 4)
        pieza_caballo.__vive__ = True

        # Simular la posibilidad de movimientos del caballo
        pieza_caballo.movimientos_posibles.return_value = [(6, 5), (2, 5), (5, 6)]

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Configuro una pieza en la casilla destino, para que la pueda comer
        self.__tablero__.__tablero__[5][2] = MagicMock(spec=Pieza, __color__="blanca")

        # Llamar al método movible
        movible, posibilidades = self.__tablero__.movible(pieza_caballo)

        # Verificar que el caballo puede moverse a sus posiciones posibles
        self.assertTrue(movible)
        self.assertIn((6, 5), posibilidades)
        self.assertIn((2, 5), posibilidades)
        self.assertIn((5, 6), posibilidades)

    def test_movible_torre(self):
        # Crear una pieza torre con una posición en (1, 1)
        pieza_torre = MagicMock(spec=Torre)
        pieza_torre.__nom__ = "Torre"
        pieza_torre.__color__ = "blanco"
        pieza_torre.__posicion__ = (1, 1)
        pieza_torre.__vive__ = True

        # Simular la posibilidad de movimientos de la torre
        pieza_torre.movimientos_posibles.return_value = [(1, 4), (4, 1)] # Movimiento vertical y horizontal

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Configuro una pieza que bloquee el camino de la torre, para sacar una de las posibilidades
        self.__tablero__.__tablero__[3][1] = MagicMock(spec=Pieza, __color__="blanca")

        # Llamar al método movible
        movible, posibilidades = self.__tablero__.movible(pieza_torre)

        # Verificar que la torre puede moverse a sus posiciones posibles
        self.assertTrue(movible)
        self.assertNotIn((1, 4), posibilidades)
        self.assertIn((4, 1), posibilidades)
        
    def test_movible_errores(self):
        # Crear una pieza con estado no viva y una que tiene posiciones fuera del tablero
        pieza_no_viva = MagicMock(spec=Peon)
        pieza_no_viva.__nom__ = "P"
        pieza_no_viva.__color__ = "blanco"
        pieza_no_viva.__posicion__ = (3, 3)
        pieza_no_viva.__vive__ = False

        pieza_fuera_tablero = MagicMock(spec=Peon)
        pieza_fuera_tablero.__nom__ = "P"
        pieza_fuera_tablero.__color__ = "blanco"
        pieza_fuera_tablero.__posicion__ = (3, 3)
        pieza_fuera_tablero.__vive__ = True
        pieza_fuera_tablero.movimientos_posibles = MagicMock(return_value=[(0, 0), (9, 9)])  # Fuera del tablero

        self.__tablero__.__tablero__ = [[MagicMock(spec=Espacio) for _ in range(10)] for _ in range(10)]

        # Test pieza no viva
        movible, posibilidades = self.__tablero__.movible(pieza_no_viva)
        self.assertFalse(movible)
        self.assertEqual(posibilidades, [])

        # Test pieza fuera del tablero
        movible, posibilidades = self.__tablero__.movible(pieza_fuera_tablero)
        self.assertFalse(movible)
        self.assertEqual(posibilidades, [])

    def test_mover_pieza(self):
        pieza = self.__tablero__.__BD_piezas__.search('P1')
        movido = self.__tablero__.mover_pieza(pieza, 'a3', [(1, 6)])
        self.assertTrue(movido)
    
    def test_mover_pieza_comer(self):
        pieza_mock = MagicMock(spec=Peon)
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__color__ = "blanca"
        pieza_mock.__posicion__ = (3, 3)
        pieza_mock.__vive__ = True
        self.__BD_piezas__.add(pieza_mock)
        
        movido = self.__tablero__.mover_pieza(pieza_mock, 'd7', [(4, 2)])
        self.assertTrue(movido)

    def test_mover_pieza_errores(self):
        pieza_mock = MagicMock(spec=Peon)
        pieza_mock.__nom__ = "Peon"
        pieza_mock.__color__ = "blanca"
        pieza_mock.__posicion__ = (3, 3)
        pieza_mock.__vive__ = True
        self.__BD_piezas__.add(pieza_mock)
        
        movido = self.__tablero__.mover_pieza(pieza_mock, 'a3', [(1, 8)])
        self.assertFalse(movido)

        movido = self.__tablero__.mover_pieza(pieza_mock, 'a', [(1, 6)])
        self.assertRaises(ValueError)

    def test_conversion_coordenadas(self):
        x, y = self.__tablero__.conversion_coordenadas(1, 8)
        self.assertEqual((x, y), ('a', '1'))
    
    def test_victoria_por_movimientos_empate(self):
        # Todas las piezas se quedan sin movimientos posibles
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_movimientos_negras_ganan(self):
        # Todas las piezas blancas se quedan sin movimientos posibles
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[(3, 3)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_movimientos_blancas_ganan(self):
        # Todas las piezas negras se quedan sin movimientos posibles
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[])
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[(2, 2)])

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_piezas_blancas_ganan(self):
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_victoria_por_piezas_negras_ganan(self):
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'blanca':
                pieza.__vive__ = False

        with self.assertRaises(SystemExit):
            self.__tablero__.verificar_victoria()

    def test_verificar_victoria_none(self):
        # Mockear las piezas vivas y sus movimientos para que ambos tengan movimientos
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            pieza.__vive__ = True
        
        for pieza in self.__tablero__.__BD_piezas__.__base_datos__.values():
            if pieza.__color__ == 'negra':
                pieza.movimientos_posibles = MagicMock(return_value=[(3 ,3)])
            if pieza.__color__ == 'blanca':
                pieza.movimientos_posibles = MagicMock(return_value=[(2, 2)])

        result = self.__tablero__.verificar_victoria()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

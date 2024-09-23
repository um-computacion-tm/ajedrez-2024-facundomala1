from game.cli import Cliente
import unittest
from unittest.mock import patch
from io import StringIO
import os
from game.cheess import Chess
from game.exeptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, InvalidMove, IndexErrorPersonalizada


class TestCli(unittest.TestCase):

    def test_inicializar_chess(self): 
        cliente = Cliente()
        self.assertIsNotNone(cliente.inicializar_chess()) 

    @patch('builtins.input', side_effect=['1', '0', '3', '0'])
    def test_funcion_entrada_valid_input(self, mock_input):
        # Simulamos una entrada de usuario válida
        cliente = Cliente()  # Asumiendo que Cliente es la clase que contiene funcion_entrada
        resultado = cliente.funcion_entrada()
        self.assertEqual(resultado, [1, 0, 3, 0])

    @patch('builtins.input', side_effect=['999', '0', '0', '0'])
    def test_input_fin_partida(self, mock_input):
        # Simulamos una entrada de usuario válida
        cliente = Cliente()  # Asumiendo que Cliente es la clase que contiene funcion_entrada
        resultado = cliente.funcion_entrada()
        self.assertEqual(resultado, False)

    def test_limpiar_consola(self):
        # Verificar que la función limpia la consola en Windows
        os.name = 'nt'
        self.assertEqual(Cliente.limpiar_consola(self), None)
        # Verificar que la función limpia la consola en Linux/macOS
        os.name = 'linux'
        self.assertEqual(Cliente.limpiar_consola(self), None)

    @patch('sys.stdout', new_callable=StringIO)
    def test_comenzar_iteracion(self, mock_stdout):
        cliente = Cliente()
        chess = Chess()
        positions = chess.get_board().get_positions()
        self.assertEqual(cliente.comenzar_iteracion(chess, positions), None)

    def test_buscar_error_indice(self):
        cliente = Cliente()
        # Verificamos que se lanza la excepción para el índice 0
        with self.assertRaises(IndexErrorPersonalizada):
            cliente.buscar_error_indice(-1)
        # Verificamos que se lanza la excepción para el índice 8
        with self.assertRaises(IndexErrorPersonalizada):
            cliente.buscar_error_indice(8)

    def test_detectar_exepcion(self):
        cliente = Cliente()
        # Verificamos que se lanza la excepción para el índice 0
        with self.assertRaises(ColorIncorrecto):
            cliente.detectar_exepcion("ColorIncorrecto")
        # Verificamos que se lanza la excepción para el índice 8
        with self.assertRaises(InvalidMove):
            cliente.detectar_exepcion("InvalidMove")
        with self.assertRaises(CasillaOcupada):
            cliente.detectar_exepcion("CasillaOcupada")
        with self.assertRaises(PiezaNoExiste):
            cliente.detectar_exepcion("PiezaNoExiste")
        with self.assertRaises(MismaCasilla):
            cliente.detectar_exepcion("MismaCasilla")
import unittest
from game.rook import Rook
from .test_move import TestUtils

class TestRook(unittest.TestCase):

    def setUp(self):
        self.rook = Rook("WHITE")  # Crea un objeto Rook blanco para usar en las pruebas

    def check_movement(self, start_row, start_col, end_row, end_col, expected_result):
        self.assertEqual(self.rook.horizontal_or_vertical_movement(start_row, end_row, start_col, end_col), expected_result)

    def test_init(self):
        # Verifica que rook es una instancia de Rook
        self.assertIsInstance(self.rook, Rook)

    def test_rook_str(self):
        utils = TestUtils()
        utils.check_piece_str(self, Rook, "♖", "♜")

    def test_horizontal(self):
        # Movimiento horizontal válido
        self.check_movement(0, 0, 0, 6, "horizontal")

    def test_vertical(self):
        # Movimiento vertical válido
        self.check_movement(0, 0, 6, 0, "vertical")

    def test_invalid(self):
        # Movimiento inválido (diagonal en este caso)
        self.check_movement(0, 0, 1, 1, "invalid")

    def test_is_valid_movement(self):
        # Prueba movimiento horizontal válido
        self.assertTrue(self.rook.is_valid_movement(0, 0, 0, 7))
        # Prueba movimiento vertical válido
        self.assertTrue(self.rook.is_valid_movement(0, 0, 7, 0))
        # Prueba movimiento inválido (diagonal)
        self.assertFalse(self.rook.is_valid_movement(0, 0, 1, 1))

if __name__ == "__main__":
    unittest.main()
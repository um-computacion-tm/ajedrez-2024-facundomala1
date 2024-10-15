import unittest
from game.bishop import Bishop
from test.test_move import TestUtils

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.bishop = Bishop("WHITE")

    def test_bishop_str(self):
        utils = TestUtils()
        utils.check_piece_str(self, Bishop, "♗", "♝")

    def test_init(self):
        bishop = Bishop("WHITE")
        self.assertIsInstance(bishop, Bishop)
        self.assertEqual(bishop.__color__, "WHITE")
        
        bishop_black = Bishop("BLACK")
        self.assertEqual(bishop_black.__color__, "BLACK")

    def test_is_valid_movement(self):
        # Movimientos válidos
        self.assertTrue(self.bishop.is_valid_movement(0, 0, 7, 7))  # Diagonal ascendente derecha
        self.assertTrue(self.bishop.is_valid_movement(7, 7, 0, 0))  # Diagonal descendente izquierda
        self.assertTrue(self.bishop.is_valid_movement(0, 7, 7, 0))  # Diagonal ascendente izquierda
        self.assertTrue(self.bishop.is_valid_movement(7, 0, 0, 7))  # Diagonal descendente derecha
        self.assertTrue(self.bishop.is_valid_movement(3, 3, 5, 5))  # Movimiento corto

        # Movimientos inválidos
        self.assertFalse(self.bishop.is_valid_movement(0, 0, 0, 7))  # Horizontal
        self.assertFalse(self.bishop.is_valid_movement(0, 0, 7, 0))  # Vertical
        self.assertFalse(self.bishop.is_valid_movement(0, 0, 2, 1))  # Movimiento de caballo

if __name__ == '__main__':
    unittest.main()
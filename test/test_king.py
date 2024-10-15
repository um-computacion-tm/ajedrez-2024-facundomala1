import unittest
from game.king import King

class TestKing(unittest.TestCase):
    def setUp(self):
        self.king = King("white")

    def test_valid_movement_up(self):
        # Moverse una casilla hacia arriba debería ser válido
        self.assertTrue(self.king.is_valid_movement(4, 3, 4, 4))

    def test_valid_movement_down(self):
        # Moverse una casilla hacia abajo debería ser válido
        self.assertTrue(self.king.is_valid_movement(4, 5, 4, 4))

    def test_valid_movement_left(self):
        # Moverse una casilla a la izquierda debería ser válido
        self.assertTrue(self.king.is_valid_movement(4, 4, 4, 3))

    def test_valid_movement_right(self):
        # Moverse una casilla a la derecha debería ser válido
        self.assertTrue(self.king.is_valid_movement(4, 4, 4, 5))

    def test_valid_movement_diagonal(self):
        # Moverse una casilla en diagonal debería ser válido
        self.assertTrue(self.king.is_valid_movement(4, 3, 3, 4))

    def test_invalid_movement_too_far(self):
        # Moverse más de una casilla debería ser inválido
        self.assertFalse(self.king.is_valid_movement(4, 2, 4, 4))

    def test_invalid_no_movement(self):
        # Quedarse en la misma casilla debería ser inválido
        self.assertFalse(self.king.is_valid_movement(4, 4, 4, 4))

if __name__ == "__main__":
    unittest.main()
import unittest
from game.queen import Queen  # Asegúrate de importar correctamente tu clase Queen

class TestQueen(unittest.TestCase):
    
    def setUp(self):
        # Crear una instancia de Queen para usar en los tests
        self.queen = Queen("white")  

    def test_valid_movement_vertical(self):
        # Moverse varias casillas hacia arriba debería ser válido
        self.assertTrue(self.queen.is_valid_movement(4, 1, 4, 4))

    def test_valid_movement_horizontal(self):
        # Moverse varias casillas a la derecha debería ser válido
        self.assertTrue(self.queen.is_valid_movement(4, 4, 4, 7))

    def test_valid_movement_diagonal(self):
        # Moverse varias casillas en diagonal debería ser válido
        self.assertTrue(self.queen.is_valid_movement(4, 1, 4, 7))

    def test_invalid_movement(self):
        # Un movimiento inválido que no sea en línea recta ni diagonal debería ser inválido
        self.assertFalse(self.queen.is_valid_movement(0, 1, 2, 0))


if __name__ == "__main__":
    unittest.main()
import unittest
from game.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.knight = Knight("WHITE")  # Crea un objeto Knight blanco para usar en las pruebas

    def test_init(self):
        # Crea un objeto Knight de color blanco
        white_knight = Knight("WHITE")
        # Verifica que se ha inicializado correctamente como un objeto Knight
        self.assertEqual(white_knight.__color__, "WHITE")
        self.assertEqual(str(white_knight), "♘")  # Verifica la representación del caballo blanco
        
        # Crea un objeto Knight de color negro
        black_knight = Knight("BLACK")
        # Verifica que se ha inicializado correctamente como un objeto Knight
        self.assertEqual(black_knight.__color__, "BLACK")
        self.assertEqual(str(black_knight), "♞")  # Verifica la representación del caballo negro

    
    def test_valid_movement(self):
        white_knight = Knight("WHITE")
        # Movimientos válidos en forma de L
        self.assertTrue(white_knight.is_valid_movement(0, 1, 2, 0))  # Dos casillas verticales y una horizontal
        self.assertTrue(white_knight.is_valid_movement(0, 1, 2, 0))  # (0, 1) a (2, 0)
        self.assertTrue(white_knight.is_valid_movement(0, 1, 2, 2))  # (0, 1) a (2, 2)
        self.assertTrue(white_knight.is_valid_movement(0, 1, 1, 3))  # (0, 1) a (1, 3)

    def test_invalid_movement(self):
        # Movimientos inválidos que no forman una "L"
        self.assertFalse(self.knight.is_valid_movement(0, 3, 0, 1))  # Movimiento inválido





if __name__ == "__main__":
    unittest.main()
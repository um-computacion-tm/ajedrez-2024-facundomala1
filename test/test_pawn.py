import unittest
from game.pawn import Pawn
from test.test_move import TestUtils

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn("WHITE")
        self.black_pawn = Pawn("BLACK")

    def test_pawn_str(self):
        utils = TestUtils()
        utils.check_piece_str(self, Pawn, "♙", "♟")

    def test_init(self):
        self.assertIsInstance(self.white_pawn, Pawn)
        self.assertEqual(self.white_pawn.__color__, "WHITE")
        self.assertTrue(self.white_pawn.__first_move__)

        self.assertIsInstance(self.black_pawn, Pawn)
        self.assertEqual(self.black_pawn.__color__, "BLACK")
        self.assertTrue(self.black_pawn.__first_move__)

    def test_is_valid_movement(self):
        self._test_pawn_movement(self.black_pawn, 1, 2, 3, 0)

    def _test_pawn_movement(self, pawn, start_row, one_step, two_step, back_step):
        # Primer movimiento
        self.assertTrue(pawn.is_valid_movement(start_row, 0, one_step, 0))  # Un paso adelante
        self.assertTrue(pawn.is_valid_movement(start_row, 0, two_step, 0))  # Dos pasos adelante
        self.assertFalse(pawn.is_valid_movement(start_row, 0, two_step + 1, 0))  # Tres pasos adelante (inválido)

        # Movimiento diagonal (captura)
        self.assertTrue(pawn.is_valid_movement(start_row, 0, one_step, 1, is_capture=True))  # Captura a la derecha
        self.assertTrue(pawn.is_valid_movement(start_row, 1, one_step, 0, is_capture=True))  # Captura a la izquierda
        self.assertFalse(pawn.is_valid_movement(start_row, 0, one_step, 1, is_capture=False))  # Diagonal sin captura (inválido)

        # Movimientos inválidos
        self.assertFalse(pawn.is_valid_movement(start_row, 0, start_row, 1))  # Movimiento lateral
        self.assertFalse(pawn.is_valid_movement(start_row, 0, back_step, 0))  # Movimiento hacia atrás

        # Después del primer movimiento
        pawn.complete_move()
        self.assertTrue(pawn.is_valid_movement(one_step, 0, two_step, 0))  # Un paso adelante
        self.assertFalse(pawn.is_valid_movement(one_step, 0, two_step + 1, 0))  # Dos pasos adelante (ya no válido)

    def test_complete_move(self):
        self.assertTrue(self.white_pawn.__first_move__)
        self.white_pawn.complete_move()
        self.assertFalse(self.white_pawn.__first_move__)

        self.assertTrue(self.black_pawn.__first_move__)
        self.black_pawn.complete_move()
        self.assertFalse(self.black_pawn.__first_move__)

if __name__ == '__main__':
    unittest.main()
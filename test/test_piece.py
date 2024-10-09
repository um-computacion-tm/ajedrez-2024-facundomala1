import unittest
from abc import ABC, abstractmethod
from game.piece import Piece

class TestPiece(unittest.TestCase):

    def test_abstract_class(self):
        # Verifica que Piece es una clase abstracta y no se puede instanciar directamente
        with self.assertRaises(TypeError):
            piece = Piece("WHITE")  # Intentar crear una instancia debe lanzar un TypeError

    def test_is_valid_movement_not_implemented(self):
        # Verifica que llamar directamente al método abstracto lanza NotImplementedError
        class TestPieceNotImplemented(Piece):
            def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
                return super().is_valid_movement(initial_row, final_row, initial_col, final_col)  # Llama al método abstracto

        piece = TestPieceNotImplemented("WHITE")
        with self.assertRaises(NotImplementedError):
            piece.is_valid_movement(0, 0, 0, 0)  # Esto debería cubrir la línea 14

    def test_is_valid_movement_abstract(self):
        # Verifica que no se puede instanciar una subclase que no implementa el método abstracto
        with self.assertRaises(TypeError):
            class TestPieceInvalid(Piece):
                pass  # No implementa is_valid_movement

            TestPieceInvalid("WHITE")  # Intentar instanciar debe lanzar TypeError

        # Verifica que una subclase que sí implementa is_valid_movement puede ser instanciada
        class TestPieceValid(Piece):
            def is_valid_movement(self, initial_row, final_row, initial_col, final_col):
                return True  # Implementación vacía solo para el test

        piece = TestPieceValid("WHITE")  # Esta clase ya puede ser instanciada
        self.assertTrue(piece.is_valid_movement(0, 0, 0, 0))



if __name__ == "__main__":
    unittest.main()
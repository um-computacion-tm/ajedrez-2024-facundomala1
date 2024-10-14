import unittest
from game.board import Board
from game.rook import Rook
from game.king import King
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.pawn import Pawn
from game.exeptions import OutOfBoardError
from unittest.mock import patch
from io import StringIO

class TestBoardSetup(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init(self):
        self.assertEqual(len(self.board.__matrix__), 8)
        for row in self.board.__matrix__:
            self.assertEqual(len(row), 8)

    def test_piece(self):
        self.assertIsInstance(self.board.__matrix__[0][0], Rook)
        self.assertIsInstance(self.board.__matrix__[0][7], Rook)
        self.assertIsInstance(self.board.__matrix__[0][1], Knight)
        self.assertIsInstance(self.board.__matrix__[0][6], Knight)
        self.assertIsInstance(self.board.__matrix__[0][2], Bishop)
        self.assertIsInstance(self.board.__matrix__[0][5], Bishop)
        self.assertIsInstance(self.board.__matrix__[0][3], Queen)
        self.assertIsInstance(self.board.__matrix__[0][4], King)
        self.assertEqual(self.board.__matrix__[0][0].__color__, "BLACK")
        self.assertEqual(self.board.__matrix__[7][3].__color__, "WHITE")

class TestBoardHelperMethods(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_out_of_board(self):
        self.assertFalse(self.board.is_out_of_board(0, 0))
        self.assertFalse(self.board.is_out_of_board(7, 7))
        
        with self.assertRaises(OutOfBoardError):
            self.board.is_out_of_board(-1, 0)
        
        with self.assertRaises(OutOfBoardError):
            self.board.is_out_of_board(0, 8)

    def test_get_color(self):
        self.assertEqual(self.board.get_color(7, 3), "WHITE")
        self.assertEqual(self.board.get_color(0, 0), "BLACK")

    def test_has_piece(self):
        self.assertTrue(self.board.has_piece(0, 0))
        self.assertFalse(self.board.has_piece(4, 4))


class TestBoardPathClear(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_path_clear(self):
        self.assertTrue(self.board.is_path_clear(3, 0, 3, 7, 'horizontal'))

    def test_is_path_clear_blocked(self):
            test_cases = [
                # start_row, start_col, end_row, end_col, block_row, block_col, direction
                (0, 0, 0, 3, 0, 2, "horizontal"),
                (0, 0, 3, 0, 2, 0, "vertical"),
                (0, 0, 3, 3, 2, 2, "diagonal"),
            ]

            for start_row, start_col, end_row, end_col, block_row, block_col, direction in test_cases:
                with self.subTest(f"{direction} from ({start_row},{start_col}) to ({end_row},{end_col})"):
                    self.board.__matrix__[block_row][block_col] = Pawn("BLACK")
                    self.assertFalse(self.board.is_path_clear(start_row, start_col, end_row, end_col, direction))
    
    def test_is_path_clear_invalid_movement(self):
        self.assertFalse(self.board.is_path_clear(0, 0, 2, 1, "invalid"))
    

class TestBoardDisplay(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_display_board(self):
        expected_output = (
            "    0   1   2   3   4   5   6   7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "0 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | 0\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "1 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | 1\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "2 |   |   |   |   |   |   |   |   | 2\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "3 |   |   |   |   |   |   |   |   | 3\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "4 |   |   |   |   |   |   |   |   | 4\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "5 |   |   |   |   |   |   |   |   | 5\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "6 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | 6\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "7 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | 7\n"
            "  +---+---+---+---+---+---+---+---+\n"
            "    0   1   2   3   4   5   6   7\n"
        )

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.board.display_board()
            actual_output = fake_output.getvalue()

        self.assertEqual(actual_output, expected_output)

class TestBoardMovement(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_move_piece_capture(self):
        self.board.__matrix__[3][3] = Pawn("BLACK")
        self.board.move_piece(6, 3, 3, 3)
        self.assertIsInstance(self.board.__matrix__[3][3], Pawn)
        self.assertEqual(self.board.__matrix__[3][3].__color__, "WHITE")

    def test_move_piece_pawn___first_move__(self):
        pawn = self.board.__matrix__[6][0]
        self.board.move_piece(6, 0, 4, 0)
        self.assertFalse(pawn.__first_move__)

class TestBoardCaptures(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        capture_counts = self.board.get_capture_counts()
        self.assertEqual(capture_counts["__white_captures__"], 2)
        self.assertEqual(capture_counts["__black_captures__"], 3)

    def test_update_capture_count(self):
        initial_white_captures = self.board.__white_captures__
        initial_black_captures = self.board.__black_captures__
        
        self.board.update_capture_count("WHITE")
        self.assertEqual(self.board.__black_captures__, initial_black_captures + 1)
        
        self.board.update_capture_count("BLACK")
        self.assertEqual(self.board.__white_captures__, initial_white_captures + 1)

class TestBoardAdditional(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_valid_move(self):
        # Prueba para movimiento fuera del tablero
        self.assertFalse(self.board.is_valid_move(8, 0, 9, 0))
        
        # Prueba para mover una pieza que no existe
        self.assertFalse(self.board.is_valid_move(3, 3, 4, 4))
        
        # Prueba para un movimiento válido de un peón
        self.assertTrue(self.board.is_valid_move(6, 0, 5, 0))
        
        # Prueba para un movimiento válido de un caballo
        self.assertTrue(self.board.is_valid_move(7, 1, 5, 2))
        
        # Prueba para un movimiento diagonal inválido del peón (sin captura)
        self.assertFalse(self.board.is_valid_move(6, 0, 5, 1))
        
        # Prueba para un movimiento diagonal válido del peón (con captura)
        # Primero, coloca una pieza enemiga en la posición de captura
        self.board.__matrix__[5][1] = Pawn("BLACK")
        self.assertTrue(self.board.is_valid_move(6, 0, 5, 1))

    def test_move_piece(self):
        # Mover un peón
        self.board.move_piece(6, 0, 4, 0)
        self.assertIsInstance(self.board.__matrix__[4][0], Pawn)
        self.assertIsNone(self.board.__matrix__[6][0])

        # Capturar una pieza
        self.board.__matrix__[3][0] = Pawn("BLACK")
        self.board.move_piece(4, 0, 3, 0)
        self.assertIsInstance(self.board.__matrix__[3][0], Pawn)
        self.assertEqual(self.board.__matrix__[3][0].__color__, "WHITE")
        

    
class TestBoardAdditionalCoverage(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_king_capture(self):
        # Colocar un rey negro en una posición vulnerable
        self.board.__matrix__[4][4] = King("BLACK")
        
        # Mover una pieza blanca para capturar al rey
        self.board.__matrix__[5][5] = Pawn("WHITE")
        self.board.move_piece(5, 5, 4, 4)
        
        self.assertTrue(self.board.__king_captured__)

    def test_get_capture_counts(self):
        self.board.__white_captures__ = 2
        self.board.__black_captures__ = 3
        
        capture_counts = self.board.get_capture_counts()
        
        self.assertEqual(capture_counts['__white_captures__'], 2)
        self.assertEqual(capture_counts['__black_captures__'], 3)

    def test_is_path_clear_for_non_knight(self):
        # Limpiar el camino para la prueba
        self.board.__matrix__[6][3] = None
        self.board.__matrix__[5][4] = None
        
        # Probar con un movimiento diagonal
        bishop = Bishop("WHITE")
        self.assertTrue(self.board.is_path_clear_for_non_knight(bishop, 7, 2, 5, 4))
        
        # Bloquear el camino y probar de nuevo
        self.board.__matrix__[6][3] = Pawn("WHITE")
        self.assertFalse(self.board.is_path_clear_for_non_knight(bishop, 7, 2, 5, 4))

    def test_are_positions_valid(self):
        # Posiciones validas
        self.assertTrue(self.board.are_positions_valid(0, 0, 1, 0))
        
        # Posición fuera del tablero
        self.assertFalse(self.board.are_positions_valid(0, 0, 8, 0))
        
        # Posición inicial sin pieza
        self.board.__matrix__[4][4] = None
        self.assertFalse(self.board.are_positions_valid(4, 4, 5, 5))

    def test_get_movement_type(self):
        self.assertEqual(self.board.get_movement_type(0, 0, 0, 3), "horizontal")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 0), "vertical")
        self.assertEqual(self.board.get_movement_type(0, 0, 3, 3), "diagonal")
        self.assertEqual(self.board.get_movement_type(0, 0, 1, 2), "invalid")
    

    def test_is_valid_move_knight(self):
        # Prueba para movimiento valido de un caballo 
        self.assertTrue(self.board.is_valid_move(7, 1, 5, 2))


    def test_handle_pawn_promotion_all_choices(self):
        for choice in ['1', '2', '3', '4', '5']:
            with self.subTest(choice=choice):
                self.board.__matrix__[0][0] = Pawn("WHITE")
                promoted_piece = self.board.handle_pawn_promotion(0, 0, choice)
                self.assertIsNotNone(promoted_piece)
                self.assertNotIsInstance(self.board.__matrix__[0][0], Pawn)
    
    def test_move_piece_invalid_capture(self):
        # Intentar capturar una pieza del mismo color
        self.board.__matrix__[5][5] = Pawn("WHITE")
        result, _ = self.board.move_piece(6, 5, 5, 5)
        self.assertEqual(result, "INVALID_CAPTURE")
    
    def test_move_piece_king_capture(self):
        # Capturar un rey 
        self.board.__matrix__[4][4] = King("BLACK")
        self.board.__matrix__[5][5] = Pawn("WHITE")
        result, color = self.board.move_piece(5, 5, 4, 4)
        self.assertEqual(result, "KING_CAPTURED")
        self.assertEqual(color, "BLACK")
        self.assertTrue(self.board.__king_captured__)
    
    def test_pawn_promotion(self):
        # Promoción de peon 
        self.board.__matrix__[1][0] = Pawn("WHITE")
        result, promotion_info = self.board.move_piece(1, 0, 0, 0)
        self.assertEqual(result, "PROMOTION_NEEDED")
        self.assertEqual(promotion_info, (0, 0))

        # Probar todas las opciones de promocion
        for choice in ['1', '2', '3', '4', '5']:
            with self.subTest(choice=choice):
                promoted_piece = self.board.handle_pawn_promotion(0, 0, choice)
                self.assertIsNotNone(promoted_piece)
                self.assertNotIsInstance(self.board.__matrix__[0][0], Pawn)
    
    def test_is_valid_move_edge_cases(self):
        # Movimiento fuera del tablero 
        self.assertFalse(self.board.is_valid_move(7, 7, 8, 8))

        # Movimiento a una posicion ocupada por una pieza del mismo color
        self.assertFalse(self.board.is_valid_move(7, 0, 7, 1))

        # Movimiento diagonal invalido para una torre 
        self.board.__matrix__[4][4] = Rook("WHITE")
        self.assertFalse(self.board.is_valid_move(4, 4, 5, 5))

        # Movimiento invalido para un caballo 
        self.assertFalse(self.board.is_valid_move(7, 1, 5, 1))

    def test_pawn_diagonal_movement(self):
        # Movimiento diagonal del peon sin captura no deberia ser valido
        self.assertFalse(self.board.is_valid_move(6, 0, 5, 1))
        self.assertFalse(self.board.is_valid_move(6, 7, 5, 6))

        # Movimiento diagonal del peon con captura deberia ser valido
        self.board.__matrix__[5][1] = Pawn("BLACK")
        self.assertTrue(self.board.is_valid_move(6, 0, 5, 1))

        # Movimiento diagonal del peon negro sin captura no deberia ser valido
        self.assertFalse(self.board.is_valid_move(1, 0, 2, 1))
        self.assertFalse(self.board.is_valid_move(1, 7, 2, 6))

        # Movimiento diagonal del peon negro con captura deberia ser valido
        self.board.__matrix__[2][1] = Pawn("WHITE")
        self.assertTrue(self.board.is_valid_move(1, 0, 2, 1))

        # Verificar que el peon no puede moverse diagonalmente mas de una casilla
        self.board.__matrix__[4][2] = Pawn("BLACK")
        self.assertFalse(self.board.is_valid_move(6, 0, 4, 2))
                

if __name__ == '__main__':
    unittest.main()
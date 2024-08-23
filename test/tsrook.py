import unittest
from game.rook import Rook
from game.piece import Piece

class MockBoard:
    def __init__(self, pieces):
        self.pieces = pieces

    def get_piece(self, row, col):
        return self.pieces.get((row, col), None)

class TestRook(unittest.TestCase):
    def setUp(self):
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")
        self.white_rook.position = (0, 0)
        self.black_rook.position = (7, 7)

    def test_str(self):
        self.assertEqual(str(self.white_rook), "♜")
        self.assertEqual(str(self.black_rook), "♖")

    def test_valid_move(self):
        # Test horizontal move
        board = MockBoard({})
        self.assertTrue(self.white_rook.is_valid_move(0, 5, board))
        self.assertTrue(self.black_rook.is_valid_move(7, 0, board))

        # Test vertical move
        self.assertTrue(self.white_rook.is_valid_move(5, 0, board))
        self.assertTrue(self.black_rook.is_valid_move(0, 7, board))

        # Test invalid move (diagonal)
        self.assertFalse(self.white_rook.is_valid_move(5, 5, board))
        self.assertFalse(self.black_rook.is_valid_move(0, 0, board))

        # Test move with pieces in the way
        board_with_pieces = MockBoard({(0, 3): Piece("WHITE"), (5, 0): Piece("BLACK")})
        self.assertFalse(self.white_rook.is_valid_move(0, 5, board_with_pieces))
        self.assertFalse(self.white_rook.is_valid_move(5, 0, board_with_pieces))

if __name__ == '__main__':
    unittest.main()
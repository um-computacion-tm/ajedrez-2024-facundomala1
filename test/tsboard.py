import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_rook_positions(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

    def test_empty_positions(self):
        self.assertIsNone(self.board.get_piece(3, 3))
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_add_piece(self):
        new_rook = Rook("WHITE", position=(4, 4))
        self.board.__positions__[4][4] = new_rook
        self.assertEqual(self.board.get_piece(4, 4), new_rook)

    def test_remove_piece(self):
        self.board.__positions__[7][0] = None
        self.assertIsNone(self.board.get_piece(7, 0))

if __name__ == '__main__':
    unittest.main()

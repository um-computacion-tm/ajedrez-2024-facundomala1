import unittest
from game.piece import Piece
class TestPiece(unittest.TestCase):

    def test_color(self):
        piece = Piece("Piece","White")
        self.assertEqual(piece.get_color(), "White")

    def test_name(self):
        piece = Piece("Piece","White")
        self.assertEqual(piece.get_name(), "Piece")
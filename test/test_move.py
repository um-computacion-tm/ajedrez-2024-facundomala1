import unittest
class TestUtils(unittest.TestCase):
    def check_piece_str(self, test_case, piece, expected_white, expected_black):
        test_case.assertEqual(str(piece("WHITE")), expected_white)
        test_case.assertEqual(str(piece("BLACK")), expected_black)
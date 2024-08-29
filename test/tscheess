import unittest
from game.cheess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.__chess__ = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.__chess__.get_turn(), "WHITE")

    def test_change_turn(self):
        self.__chess__.__change_turn__()
        self.assertEqual(self.__chess__.get_turn(), "BLACK")
        self.__chess__.__change_turn__()
        self.assertEqual(self.__chess__.get_turn(), "WHITE")

    def test_move(self):
        # Test valid move
        self.__chess__.move(1, 0, 3, 0)
        self.assertEqual(self.__chess__.get_turn(), "BLACK")
        # Test invalid move
        self.__chess__.move(3, 0, 4, 0)
        self.assertEqual(self.__chess__.get_turn(), "BLACK")


    def test_show_board(self):
        self.assertIsInstance(self.__chess__.show_board(), str)

if __name__ == '__main__':
    unittest.main()
from game.piece import Piece

class Knight(Piece):
    __white_str__ = '♘'
    __black_str__ = '♞'
    def __init__(self, name, color):
        super().__init__(name, color)

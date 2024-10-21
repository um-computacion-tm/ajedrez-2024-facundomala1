# Knight (Caballo)
from .piece import Piece
class Knight(Piece):
    def __init__(self, __color__):
        super().__init__(__color__)
    def __str__(self):
        return "♘" if self.__color__ == "WHITE" else "♞"
    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        row_difference = abs(final_row - initial_row)
        col_difference = abs(final_col - initial_col)
        
        if (row_difference == 2 and col_difference == 1) or (row_difference == 1 and col_difference == 2):
            return True
        return False
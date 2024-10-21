# Queen (Reina)
from game.piece import Piece


class Queen(Piece):
    def __init__(self, __color__):
        super().__init__(__color__)
    
    def __str__(self):
        return "♕" if self.__color__ == "WHITE" else "♛"



    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        row_diff = abs(final_row - initial_row)
        col_diff = abs(final_col - initial_col)
        
        # La reina se puede mover cualquier número de casillas en línea recta o diagonal
        # Movimiento horizontal, vertical o diagonal
        if row_diff == col_diff or initial_row == final_row or initial_col == final_col:
            #print("Debug: Valid queen movement")
            return True
        else:
            #print("Debug: Invalid queen movement")
            return False
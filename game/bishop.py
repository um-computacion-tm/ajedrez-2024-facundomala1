# Bishop (Alfil)
# Movimiento: El alfil se mueve diagonalmente, tantas casillas como desee.

from .piece import Piece

class Bishop(Piece):
    def __init__(self, __color__):
        super().__init__(__color__)
    
    def __str__(self):
        return "♗" if self.__color__ == "WHITE" else "♝"
    

    
    # Verifica si el movimiento es diagonal comparando las diferencias absolutas entre filas y columnas
    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        if abs(final_row - initial_row) == abs(final_col - initial_col):
            return True
        else:
            return False
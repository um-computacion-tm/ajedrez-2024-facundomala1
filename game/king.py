# King (Rey):
# Movimiento: El rey se mueve una casilla en cualquier dirección: 
# horizontal, vertical o diagonal.

from game.piece import Piece

class King(Piece):

    def __init__(self, __color__):
        super().__init__(__color__)
    
    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        # Calcular la diferencia absoluta en filas y columnas
        row_diff = abs(final_row - initial_row)
        col_diff = abs(final_col - initial_col)
        
        #print(f"Debug: King movement from ({initial_row}, {initial_col}) to ({final_row}, {final_col})")
        #print(f"Debug: row_diff = {row_diff}, col_diff = {col_diff}")
        
        # El rey puede moverse una casilla en cualquier dirección
        # Por lo tanto, la diferencia máxima en filas y columnas debe ser 1
        if row_diff <= 1 and col_diff <= 1 and (row_diff != 0 or col_diff != 0):
            #print("Debug: Valid king movement")
            return True
        else:
            #print("Debug: Invalid king movement")
            return False

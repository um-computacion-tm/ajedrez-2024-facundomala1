# Pawn(Peón)
# Movimiento: Los peones se mueven una casilla hacia adelante,
# pero capturan en diagonal. En su primer movimiento, un peón 
# puede avanzar dos casillas.

from .piece import Piece


class Pawn(Piece):
    def __init__(self, __color__):
        super().__init__(__color__) # Hereda de la clase padre Piece
        self.__first_move__ = True # Indica si es el primer movimiento, lo inicializa asi

    def __str__(self):
        return "♙" if self.__color__ == "WHITE" else "♟"

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col, is_capture=False):
        # Determinar la dirección del movimiento según el __color__
        
        direction = 1 if self.__color__.lower() == "black" else -1
        flag = False
        # Calcular la diferencia en filas y columnas
        row_diff = final_row - initial_row
        col_diff = abs(final_col - initial_col)

        # Movimiento hacia adelante
        if col_diff == 0:
            if self.__first_move__:
                # Primer movimiento: puede avanzar una o dos casillas
                valid = row_diff == direction or row_diff == 2 * direction
                return valid
            else:
                # Después del primer movimiento: solo puede avanzar una casilla
                valid = row_diff == direction
                return valid
        
        # Movimiento diagonal (potencial captura)
        elif col_diff == 1 and row_diff == direction:
            if is_capture:
                flag = True
                
            else:
                flag = False
                
        
        return flag

     # Cambia el estado de que ya no es el primer movimiento del peon
    def complete_move(self):
        if self.__first_move__:
            self.__first_move__ = False
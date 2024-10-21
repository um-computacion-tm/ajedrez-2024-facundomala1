from game.piece import Piece

class Rook(Piece):

    def __init__(self, __color__):
        super().__init__(__color__)
    
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"

    # Determina si el movimiento es horizontal o vertical
    def horizontal_or_vertical_movement(self, initial_row, final_row, initial_col, final_col):
        if initial_row == final_row and initial_col != final_col:
            return "horizontal"
        elif initial_col == final_col and initial_row != final_row:
            return "vertical"
        else:
            return "invalid"

    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        # Determinar el tipo de movimiento
        movement_type = self.horizontal_or_vertical_movement(initial_row, final_row, initial_col, final_col)
        
        if movement_type == "invalid":
            return False

        # La verificación del camino despejado se hará en el Board
        return True
from piece import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♖"
        else:
            return "♜"
    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.position
        
        # Movimiento horizontal o vertical
        if from_row != to_row and from_col != to_col:
            return False
        
        # Comprobar si hay piezas en el camino
        step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)
        
        current_row, current_col = from_row + step_row, from_col + step_col
        while (current_row, current_col) != (to_row, to_col):
            if board.get_piece(current_row, current_col) is not None:
                return False
            current_row += step_row
            current_col += step_col
        
        # La casilla de destino está vacía o contiene una pieza del oponente
        destination_piece = board.get_piece(to_row, to_col)
        return destination_piece is None or destination_piece.color != self.color
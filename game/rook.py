from piece import Piece

class Rook(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
    def is_valid_move(self, to_row, to_col, board):
        from_row, from_col = self.position
        if from_row != to_row and from_col != to_col:
            return False  # La torre solo se mueve en línea recta

        # Verificar si hay piezas en el camino
        if from_row == to_row:
            step = 1 if to_col > from_col else -1
            for col in range(from_col + step, to_col, step):
                if board.get_piece(from_row, col) is not None:
                    return False
        else:
            step = 1 if to_row > from_row else -1
            for row in range(from_row + step, to_row, step):
                if board.get_piece(row, from_col) is not None:
                    return False

        return True
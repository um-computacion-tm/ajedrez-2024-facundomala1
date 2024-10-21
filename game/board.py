from game.king import King
from game.knight import Knight
from game.queen import Queen
from game.bishop import Bishop
from game.rook import Rook
from game.pawn import Pawn
from game.piece import Piece
from game.exeptions import OutOfBoardError

class Board:

    def __init__(self):
        # Crear un tablero vacío de 8x8 y agrega las piezas en su posicion.
        self.__matrix__ = [[None for _ in range(8)] for _ in range(8)]
        self.__white_captures__ = 0  # Contador
        self.__black_captures__ = 0  # Contador
        self.__king_captured__ = False  # Indicador

        # negras
        self.__matrix__[0][0] = Rook(__color__= "BLACK") # Torre
        self.__matrix__[0][7] = Rook(__color__= "BLACK") # Torre
        self.__matrix__[0][1] = Knight(__color__= "BLACK") # Caballo
        self.__matrix__[0][6] = Knight(__color__= "BLACK") # Caballo
        self.__matrix__[0][2] = Bishop(__color__= "BLACK") # Alfil
        self.__matrix__[0][5] = Bishop(__color__= "BLACK") # Alfil
        self.__matrix__[0][3] = Queen(__color__= "BLACK") # Reina
        self.__matrix__[0][4] = King(__color__= "BLACK") # Rey
        for i in range(8):
            self.__matrix__[1][i] = Pawn(__color__= "BLACK") # Peon

        # blancas
        self.__matrix__[7][7] = Rook(__color__= "WHITE") # Torre
        self.__matrix__[7][0] = Rook(__color__= "WHITE") # Torre
        self.__matrix__[7][1] = Knight(__color__= "WHITE") # Caballo
        self.__matrix__[7][6] = Knight(__color__= "WHITE") # Caballo
        self.__matrix__[7][2] = Bishop(__color__= "WHITE") # Alfil
        self.__matrix__[7][5] = Bishop(__color__= "WHITE") # Alfil
        self.__matrix__[7][3] = Queen(__color__= "WHITE") # Reina
        self.__matrix__[7][4] = King(__color__= "WHITE") # Rey
        for i in range(8):
            self.__matrix__[6][i] = Pawn(__color__= "WHITE") # Peon
    
    def is_out_of_board(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return False
        raise OutOfBoardError(f"La posición ({row}, {col}) está fuera del tablero")

    def has_piece(self, row, col):
        return self.__matrix__[row][col] is not None

    def get_color(self, row, col):
        piece = self.__matrix__[row][col]
        return piece.__color__ if piece else None

    def is_valid_move(self, p_fila, p_columna, m_fila, m_columna):
        if not self.are_positions_valid(p_fila, p_columna, m_fila, m_columna):
            return False

        pieza = self.__matrix__[p_fila][p_columna]
        is_capture = self.is_capture_move(m_fila, m_columna, pieza)
        move_info = (pieza, p_fila, p_columna, m_fila, m_columna, is_capture)

        if not self.is_valid_piece_movement(move_info):
            return False

        if isinstance(pieza, Knight):
            return self.is_destination_valid(pieza, m_fila, m_columna)

        return self.validate_regular_move(pieza, p_fila, p_columna, m_fila, m_columna)

    def is_capture_move(self, m_fila, m_columna, pieza):
        return self.has_piece(m_fila, m_columna) and self.get_color(m_fila, m_columna) != pieza.__color__

    def validate_regular_move(self, pieza, p_fila, p_columna, m_fila, m_columna):
        movement_type = self.get_movement_type(p_fila, p_columna, m_fila, m_columna)
    
        if movement_type == "invalid" or not self.is_path_clear(p_fila, p_columna, m_fila, m_columna, movement_type):
            return False
    
        return self.is_destination_valid(pieza, m_fila, m_columna)


    def is_valid_piece_movement(self, move_info):
        pieza, p_fila, p_columna, m_fila, m_columna, is_capture = move_info
        if isinstance(pieza, Pawn):
            is_valid = pieza.is_valid_movement(p_fila, p_columna, m_fila, m_columna, is_capture)
            return is_valid and not (abs(m_columna - p_columna) == 1 and not is_capture)
        return pieza.is_valid_movement(p_fila, p_columna, m_fila, m_columna)

    def is_path_clear_for_non_knight(self, pieza, p_fila, p_columna, m_fila, m_columna):
        movement_type = self.get_movement_type(p_fila, p_columna, m_fila, m_columna)
        return self.is_path_clear(p_fila, p_columna, m_fila, m_columna, movement_type)

    def is_destination_valid(self, pieza, m_fila, m_columna):
        return not self.has_piece(m_fila, m_columna) or self.get_color(m_fila, m_columna) != pieza.__color__

    def are_positions_valid(self, p_fila, p_columna, m_fila, m_columna):
        try:
            self.is_out_of_board(p_fila, p_columna)
            self.is_out_of_board(m_fila, m_columna)
        except OutOfBoardError:
            return False
        return self.has_piece(p_fila, p_columna)

    def get_movement_type(self, p_fila, p_columna, m_fila, m_columna):
        if p_fila == m_fila:
            return "horizontal"
        if p_columna == m_columna:
            return "vertical"
        if abs(m_fila - p_fila) == abs(m_columna - p_columna):
            return "diagonal"
        return "invalid"

    def move_piece(self, p_fila, p_columna, m_fila, m_columna):
        pieza = self.__matrix__[p_fila][p_columna]
        
        if self.has_piece(m_fila, m_columna):
            pieza_capturada = self.__matrix__[m_fila][m_columna]
            color_destino = pieza_capturada.__color__
            
            if color_destino != pieza.__color__:
                if isinstance(pieza_capturada, King):
                    self.__king_captured__ = True
                    return "KING_CAPTURED", color_destino
                
                self.update_capture_count(color_destino)
                self.__matrix__[m_fila][m_columna] = None
            else:
                return "INVALID_CAPTURE", None

        self.__matrix__[p_fila][p_columna] = None
        self.__matrix__[m_fila][m_columna] = pieza

        if isinstance(pieza, Pawn):
            pieza.complete_move()
            if (pieza.__color__ == "WHITE" and m_fila == 0) or (pieza.__color__ == "BLACK" and m_fila == 7):
                return "PROMOTION_NEEDED", (m_fila, m_columna)

        return "NORMAL", None

    def handle_pawn_promotion(self, fila, columna, choice):
        pawn = self.__matrix__[fila][columna]
        color = pawn.__color__
        
        promotion_pieces = {
            "1": Queen,
            "2": Rook,
            "3": Bishop,
            "4": Knight
        }
        
        new_piece_class = promotion_pieces.get(choice, Queen)
        new_piece = new_piece_class(color)
        
        self.__matrix__[fila][columna] = new_piece
        return type(new_piece).__name__
    def update_capture_count(self, color_destino):
        if color_destino == "WHITE":
            self.__black_captures__ += 1
        else:
            self.__white_captures__ += 1

    def get_capture_counts(self):
        return {"__white_captures__": self.__white_captures__, "__black_captures__": self.__black_captures__}

    def is_path_clear(self, initial_row, initial_col, final_row, final_col, movement_type):
        if movement_type == "horizontal":
            return self._is_horizontal_path_clear(initial_row, initial_col, final_col)
        if movement_type == "vertical":
            return self._is_vertical_path_clear(initial_col, initial_row, final_row)
        if movement_type == "diagonal":
            return self._is_diagonal_path_clear(initial_row, initial_col, final_row, final_col)
        return False

    def _is_horizontal_path_clear(self, row, initial_col, final_col):
        step = 1 if final_col > initial_col else -1
        return all(self.__matrix__[row][col] is None for col in range(initial_col + step, final_col, step))

    def _is_vertical_path_clear(self, col, initial_row, final_row):
        step = 1 if final_row > initial_row else -1
        return all(self.__matrix__[row][col] is None for row in range(initial_row + step, final_row, step))

    def _is_diagonal_path_clear(self, initial_row, initial_col, final_row, final_col):
        row_step = 1 if final_row > initial_row else -1
        col_step = 1 if final_col > initial_col else -1
        row, col = initial_row + row_step, initial_col + col_step
        
        while (row != final_row) and (col != final_col):
            if self.__matrix__[row][col] is not None:
                return False
            row += row_step
            col += col_step
        
        return True

    def display_board(self):
        print("    0   1   2   3   4   5   6   7")
        print("  +" + "---+" * 8)

        for i, row in enumerate(self.__matrix__):
            row_display = [str(piece) if piece else " " for piece in row]
            print(f"{i} | " + " | ".join(row_display) + f" | {i}")
            print("  +" + "---+" * 8)
        print("    0   1   2   3   4   5   6   7")

if __name__ == "__main__":
    board = Board()
    board.display_board()
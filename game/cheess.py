from game.board import Board
class Chess:
    def __init__(self):
        self.__tablero__ = Board() # Creo objeto __board__
        self.__current_player__ = "WHITE" # Inicializo el primer jugador en blanco
        self.__mutual_agreement_to_end__ = False 

    
    def get_captures(self):
        return self.__tablero__.get_capture_counts()


    def is_over(self):
        # Un jugador se queda sin piezas (15 capturas, excluyendo el rey)
        if self.__tablero__.__white_captures__ == 15 or self.__tablero__.__black_captures__ == 15:
            return True
        
        # El rey ha sido capturado
        if self.__tablero__.__king_captured__:
            return True
        
        # Los jugadores deciden terminar la partida de mutuo acuerdo
        if self.__mutual_agreement_to_end__:
            return True
        
        return False

    # Cambia el estado de __mutual_agreement_to_end__
    def end_game_by_agreement(self):
        self.__mutual_agreement_to_end__ = True


    def display_board(self):
        self.__tablero__.display_board()



    def play_move(self, piece, move):
        p_fila, p_columna = self.parse_move(piece)
        m_fila, m_columna = self.parse_move(move)
        piece_color = self.__tablero__.get_color(p_fila, p_columna)
        
        result = "INVALID"
        info = None

        if piece_color == self.__current_player__:
            if self.__tablero__.is_valid_move(p_fila, p_columna, m_fila, m_columna):
                move_result = self.__tablero__.move_piece(p_fila, p_columna, m_fila, m_columna)
                
                if isinstance(move_result, tuple):
                    result, info = move_result
                else:
                    result = move_result

                if result == "NORMAL":
                    self.switch_turn()
                    result = "VALID"
            else:
                result = "INVALID"
        else:
            result = "INVALID_TURN"

        return (result, info) if info is not None else result

    def promote_pawn(self, fila, columna, choice):
        promoted_piece = self.__tablero__.handle_pawn_promotion(fila, columna, choice)
        self.switch_turn()
        return promoted_piece



    def parse_move(self, move):
        if len(move) != 2:
            raise ValueError("Invalid input. Please enter two digits together (e.g., '62' for row 6, column 2).")
        
        try:
            row = int(move[0])
            col = int(move[1])
            
            if 0 <= row <= 7 and 0 <= col <= 7:
                return row, col
            else:
                raise ValueError("Coordinates must be between 0 and 7.")
        except ValueError:
            raise ValueError("Please enter only numbers for coordinates.")


    # Cambio de turno
    def switch_turn(self):
        self.__current_player__ = "BLACK" if self.__current_player__ == "WHITE" else "WHITE"
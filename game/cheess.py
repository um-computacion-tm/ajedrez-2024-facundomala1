from board import Board
def main ():
    chess = Chess ()


class Chess:
    def __init__(self):
        self.board = Board()
        self.__turn__ = "WHITE"

    def move(self,from_row,from_col,to_row,to_col):
        # Validar coordenadas
        piece = self.board.get_piece(from_row, from_col)
        if piece and piece.color == self.__turn__:
            if piece.is_valid_move(to_row, to_col, self.board):
                self.board.move_piece(from_row, from_col, to_row, to_col)
                self.change_turn()
            else:
                print("Movimiento inválido")
        else:
            print("No es tu turno o no hay pieza en la posición inicial")

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

if __name__ == "__main__":
    main()
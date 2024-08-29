from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__playing__ = True

    def move(self, from_row, from_col, to_row, to_col):
        # Validar coordenadas
        piece = self.__board__.get_piece(from_row, from_col)
        if piece and piece.__color__ == self.__turn__:
            if piece.is_valid_move(to_row, to_col, self.__board__):
                self.__board__.move_piece(from_row, from_col, to_row, to_col)
                self.__change_turn__()
            else:
                print("Movimiento inválido")
        else:
            print("Movimiento inválido")

    def get_turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def __change_turn__(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def is_playing(self):
        return self.__playing__
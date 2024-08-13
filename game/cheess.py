def main ():
    chess = Chess ()


class Chess:
    def __init__(self):
        pass

    def move(self,from_row,from_col,to_row,to_col):
        #VALIDAR CORDENADAS

        piece=self.board.get_piece(from_row,from_col)
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
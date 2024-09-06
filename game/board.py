from rook import Rook
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
from pawn import Pawn
class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.___positions__.append(col)
            
        self.__positions__[0][0] = Rook("Rook","White")
        self.__positions__[0][1] = Knight("Knight","White")
        self.__positions__[0][2] = Bishop("Bishop","White")
        self.__positions__[0][3] = King("King","White")
        self.__positions__[0][4] = Queen("Queen","White")
        self.__positions__[0][5] = Bishop("Bishop","White")
        self.__positions__[0][6] = Knight("Knight","White")
        self.__positions__[0][7] = Rook("Rook","White")
        for i in range(8):
            self.__positions__[1][i] = Pawn("Pawn","White")
            self.__positions__[6][i] = Pawn("Pawn","Black")

        self.__positions__[7][0] = Rook("Rook","Black")
        self.__positions__[7][1] = Knight("Knight","Black")
        self.__positions__[7][2] = Bishop("Bishop","Black")
        self.__positions__[7][3] = King("King","Black")
        self.__positions__[7][4] = Queen("Queen","Black")
        self.__positions__[7][5] = Bishop("Bishop","Black")
        self.__positions__[7][6] = Knight("Knight","Black")
        self.__positions__[7][7] = Rook("Rook","Black")    
    def set_position(self, from_row, from_col, to_row, to_col):
        self.__positions__[to_row][to_col] = self.__positions__[from_row][from_col]
        self.__positions__[from_row][from_col] = None
    def get_piece(self, row, col):
        if self.__positions__[row][col] is None:
            return None
        return self.__positions__[row][col]

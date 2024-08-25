class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    #def get_moves(self, position):
        #raise NotImplementedError("This method should be overridden by subclasses")
class Rook:
    def __init__(self, color):
        super().__init__(color)

    def get_moves(self, position):
        moves = []
        row, col = position
        for i in range(8):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
        return moves
class Queen:
    def __init__(self, color):
        super().__init__(color)

    def get_moves(self, position):
        moves = []
        row, col = position
        for i in range(8):
            if i != row:
                moves.append((i, col))
            if i != col:
                moves.append((row, i))
            if i != row and i != col:
                if 0 <= row + i < 8 and 0 <= col + i < 8:
                    moves.append((row + i, col + i))
                if 0 <= row - i < 8 and 0 <= col - i < 8:
                    moves.append((row - i, col - i))
                if 0 <= row + i < 8 and 0 <= col - i < 8:
                    moves.append((row + i, col - i))
                if 0 <= row - i < 8 and 0 <= col + i < 8:
                    moves.append((row - i, col + i))
        return moves
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def get_moves(self, position):
        moves = []
        row, col = position
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= row + i < 8 and 0 <= col + j < 8:
                    moves.append((row + i, col + j))
        return moves

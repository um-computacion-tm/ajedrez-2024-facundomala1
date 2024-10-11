# exepciones

class ChessException(Exception):
    pass

class InvalidMoveError(ChessException):
    pass

class OutOfBoardError(ChessException):
    pass

class PieceNotFoundError(ChessException):
    pass

class SameColorCaptureError(ChessException):
    pass
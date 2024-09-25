from board import Board
from moves import ReglasDeMovimientos

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
        self.__ganador__ = None
        self.__reglas__ = ReglasDeMovimientos()
    
    def move(self, from_row, from_col, to_row, to_col):

        mensaje = ""

        origin_piece = self.__board__.get_piece(from_row, from_col)
        destination = self.__board__.get_piece(to_row, to_col)
        
        if origin_piece is None:
            mensaje = "PiezaNoExiste"

        elif origin_piece.get_color() != self.__turn__:
            mensaje = "ColorIncorrecto"
        
        elif from_row == to_row and from_col == to_col:
            mensaje = "MismaCasilla"

        elif destination is not None and destination.get_color() == self.__turn__:
            mensaje = "CasillaOcupada" 
            
        if mensaje != "":
            return(mensaje)
        
        
        return(self.habilitar_movimiento(destination, from_row, from_col, to_row, to_col))
            
    def habilitar_movimiento(self, destination, from_row, from_col, to_row, to_col):
            
        validar = self.analizar_movimiento(self.__board__.get_positions(), from_row, from_col, to_row, to_col)
        if validar == "MovimientoInvalido":
            return "MovimientoInvalido"

        if destination != None and destination.get_name() == "King" and destination.get_color() != self.__turn__:
            self.__ganador__ = self.__turn__
            return "ReyEliminado"
        
        self.__board__.set_positions(from_row, from_col, to_row, to_col)
        self.change_turn()    
        return "Valido"

    def get_reglas(self):
        return self.__reglas__

    # Funcion para cambiar el turno de la partida, cada vez que se valide un movimiento. Cambia al turno contrario.
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"

    def get_board(self):
        return self.__board__
    
    def get_turn(self):
        return self.__turn__

    def get_ganador(self):
        return self.__ganador__

    # Determinamos si el movimiento cumple con las reglas de la pieza a mover
    def analizar_movimiento(self, positions, from_row, from_col, to_row, to_col):
        nombre_pieza = positions[from_row][from_col].get_name()
        reglas = self.__reglas__

        # Movimiento Rook
        if nombre_pieza == "Rook":
            validacion = reglas.mover_perpendicularmente(positions, from_row, from_col, to_row, to_col)

        # Movimiento knight
        elif nombre_pieza == "Knight":
            validacion = reglas.mover_caballo(positions, from_row, from_col, to_row, to_col)

        # Movimiento Bishop
        elif nombre_pieza == "Bishop":
            validacion = reglas.mover_diagonalmente(positions, from_row, from_col, to_row, to_col)

        # Movimiento Queen
        elif nombre_pieza == "Queen":
            validacion = reglas.mover_reina(positions, from_row, from_col, to_row, to_col)
        
        # Movimiento King
        elif nombre_pieza == "King":
            validacion = reglas.mover_rey(positions, from_row, from_col, to_row, to_col)
        
        # Movimiento Pawn
        elif nombre_pieza == "Pawn":
            validacion = reglas.mover_peon(positions, from_row, from_col, to_row, to_col)
        
        # Puede ser "Valido" o "MovimientoInvalido"
        return validacion
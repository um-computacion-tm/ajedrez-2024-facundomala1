from math import sqrt
class ReglasDeMovimientos:
    def __init__(self):
        self.tablero = None
        pass
    def calcular_distancia(self, from_row, from_col, to_row, to_col):
        mov_fila = abs(to_row) - abs(from_row)
        mov_columna = abs(to_col) - abs(from_col) 
        return [mov_fila, mov_columna]
    def mover_diagonalmente(self, positions, from_row, from_col, to_row, to_col):
        #diagonal
        if abs(to_row - from_row) != abs(to_col - from_col):
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"
    def camino_libre(self, positions, from_row, from_col, to_row, to_col, verificar_color=False):
        # libre
        paso_fila = 1 if to_row > from_row else -1
        paso_columna = 1 if to_col > from_col else -1
    
        for i in range(1, abs(to_row - from_row)):
            fila = from_row + i * paso_fila
            columna = from_col + i * paso_columna
    
            if positions[fila][columna] is not None:
                return False
    
        if verificar_color:
            origen = positions[from_row][from_col]
            destino = positions[to_row][to_col]
            if destino is not None and destino.get_color() != origen.get_color():
                return False
    
        return True

    def mover_perpendicularmente(self, positions, from_row, from_col, to_row, to_col):
        #perpendicular
        if from_row != to_row and from_col != to_col:
            return "MovimientoInvalido"

        #libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"
    def calcular_incremento(self, valor):
        if valor == 0:
            return 0  # o algún otro valor por defecto
        incremento = int(valor / abs(valor))
        return incremento
    def mover_pieza(self, positions, from_row, from_col, to_row, to_col):
        pieza = positions[from_row][from_col]

        if pieza is None:
            return "MovimientoInvalido"

        #válido según la pieza
        if pieza.tipo == "peon":
            return self.mover_peon(positions, from_row, from_col, to_row, to_col)
        elif pieza.tipo == "caballo":
            return self.mover_caballo(positions, from_row, from_col, to_row, to_col)
        elif pieza.tipo == "alfil":
            return self.mover_alfil(positions, from_row, from_col, to_row, to_col)
        elif pieza.tipo == "torre":
            return self.mover_torre(positions, from_row, from_col, to_row, to_col)
        elif pieza.tipo == "reina":
            return self.mover_reina(positions, from_row, from_col, to_row, to_col)
        elif pieza.tipo == "rey":
            return self.mover_rey(positions, from_row, from_col, to_row, to_col)

        return "MovimientoInvalido"

    def mover_peon(self, positions, from_row, from_col, to_row, to_col):
        # válido para un peón
        if abs(to_row - from_row) > 2 or abs(to_col - from_col) > 1:
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"

    def mover_caballo(self, positions, from_row, from_col, to_row, to_col):
        # caballo
        if abs(to_row - from_row) != 2 or abs(to_col - from_col) != 1:
            return "MovimientoInvalido"

        #libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"

    def mover_alfil(self, positions, from_row, from_col, to_row, to_col):
        # válido para un alfil
        if abs(to_row - from_row) != abs(to_col - from_col):
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"

    def mover_torre(self, positions, from_row, from_col, to_row, to_col):
        # válido para una torre
        if from_row != to_row and from_col != to_col:
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"

    def mover_reina(self, positions, from_row, from_col, to_row, to_col):
        #válido para una reina
        if abs(to_row - from_row) != abs(to_col - from_col) and from_row != to_row and from_col != to_col:
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"

    def mover_rey(self, positions, from_row, from_col, to_row, to_col):
        #válido para un rey
        if abs(to_row - from_row) > 1 or abs(to_col - from_col) > 1:
            return "MovimientoInvalido"

        # libre
        if not self.camino_libre(positions, from_row, from_col, to_row, to_col):
            return "MovimientoInvalido"

        return "Valido"
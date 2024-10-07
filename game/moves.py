from math import sqrt

class ReglasDeMovimientos:
    
    def __init__(self) -> None:
        pass
    
    # Calculamos la distancia entre las casillas tanto en filas como columnas
    def calcular_distancia(self, from_row, from_col, to_row, to_col):

        mov_fila = abs(to_row) - abs(from_row)
        mov_columna = abs(to_col) - abs(from_col) 
        return [mov_fila, mov_columna]

    
    def movimiento_diagonal(chess, positions, from_row, from_col, to_row, to_col):
        reglas = ReglasDeMovimientos()
        #Calculamos la distancia entre las casilla
        distancias = reglas.calcular_distancia(from_row, from_col, to_row, to_col)
        #Detectamos aritmeticamente si el movimiento es diagonal
        if  abs(distancias[0]) == abs(distancias[1]):

            #Analizamos si alguna casilla que atraviese esta ocupada
            inputs = [from_row, from_col, to_row, to_col]

            # Analizamos si alguna casilla que atraviese esta ocupada
            return chess.analizar_camino(positions, distancias, inputs)

        return "MovimientoInvalido"


    # Analizamos si alguna casilla que atraviese esta ocupada para el metodo movimiento diagonal
    # Recibe las posiciones del tablero, las distancias en filas y columnas, y los datos de entrada
    def analizar_camino(self, positions, distancias, inputs):
        origen = positions[inputs[0]][inputs[1]]
        inc_fila = self.calcular_incremento(distancias[0])
        inc_columna = self.calcular_incremento(distancias[1])
        
        #Analizamos si alguna casilla que atraviese esta ocupada
        mensaje = "Valido"
        for casilla in range(1, abs(distancias[0]) + 1, abs(inc_fila)):

            # Si se ha llegado al final de la casilla, se detiene el bucle
            if casilla == abs(distancias[0]) and positions[inputs[2]][inputs[3]] != None:
                if positions[inputs[2]][inputs[3]].get_color() != origen.__color__:
                    mensaje = "Valido"
                    break
        
            # Si alguna de las casillas que atraviese esta ocupada, MovimientoInvalido
            if positions[inputs[0] + (casilla*inc_fila)][inputs[1] + (casilla*inc_columna)] != None:
                mensaje = "MovimientoInvalido"
                break

        return mensaje
    
    # Calculamos la distancia entre las casillas tanto en filas como columnas para el metodo analizar camino
    def calcular_incremento(self, valor):
        incremento = int(valor / abs(valor))
        return incremento
    
    # Usado para determinar los movimientos de la torre y la reina
    def movimiento_perpendicular(chess, positions, from_row, from_col, to_row, to_col):
        reglas = ReglasDeMovimientos()
        if from_row == to_row or from_col == to_col:
            
            #Movimiento horizontal
            if from_row == to_row:
                return reglas.movimiento_horizontal(positions, from_row, from_col, to_row, to_col)
                
            #Movimiento vertical
            elif from_col == to_col:
                return reglas.movimiento_vertical(positions, from_row, from_col, to_row, to_col)
            
        return "MovimientoInvalido"

    # Utilizado por Movimiento Perpendicular
    # Recibe los datos de la posicion de origen y destino y las posiciones de todo el tablero
    def movimiento_horizontal(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]
        # Determinar el incremento
        step = 1 if to_col > from_col else -1

        for i in range(from_col + step, to_col + step, step):

            if positions[from_row][i] is None:
                if i == to_col:
                    return "Valido"
                continue
                    
            if positions[from_row][i] is not None:
                if i == to_col and positions[from_row][i].get_color() != self.__color__:
                    return "Valido"
                return "MovimientoInvalido"
                
    # Utilizado por Movimiento Perpendicular
    # Recibe los datos de la posicion de origen y destino y las posiciones de todo el tablero
    def movimiento_vertical(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]
        # Determinar el incremento
        step = 1 if to_row > from_row else -1

        for i in range(from_row + step, to_row + step, step):

            if positions[i][from_col] is None:
                if i == to_row:
                    return "Valido"
                continue
                    
            if positions[i][from_col] is not None:
                if i == to_row and positions[i][from_col].get_color() != self.__color__:
                    return "Valido"
                return "MovimientoInvalido"
    

    # Movimiento del Peon
    def movimiento_pawn(chess, positions, from_row, from_col, to_row, to_col):
        
        datos = ReglasDeMovimientos.iniciar_metodo_pawn(positions, from_row, from_col, to_row, to_col)
        direccion = 1 if datos[0].get_color() == "White" else -1

        #Analizamos si es su primer movimiento para permitir que se mueva dos espacios
        if datos[0].get_initial_position() == True:
            if datos[1] == (2*direccion) and datos[2] == 0 and datos[3] == None:
                datos[0].set_initial_position(False)
                return "Valido"

        #Movimiento vertical
        if datos[1] == direccion:
            
            #Movimiento diagonal
            if datos[2] != 0 and datos[3] != None:

                if sqrt(datos[1]**2 + datos[2]**2) == sqrt(2): 
                    # Si el movimiento es diagonal, solo se valida si es para comer a otra pieza.
                    return ReglasDeMovimientos.peon_comer_pieza(datos)

            if datos[2] == 0 and datos[3] == None:
                datos[0].set_initial_position(False)
                return "Valido"
                
        return "MovimientoInvalido"
    
    # Hacemos los calculos necesarios para el movimiento de un pawn
    def iniciar_metodo_pawn(positions, from_row, from_col, to_row, to_col):
        pieza_inicial = positions[from_row][from_col]
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col
        destination = positions[to_row][to_col]
        return [pieza_inicial, mov_fila, mov_columna, destination]
    
    # Validamos si el intento de comer a otra pieza es valido
    # Datos = [pieza_inicial, mov_fila, mov_columna, destino]
    def peon_comer_pieza(datos):
        if datos[3].get_color() != datos[0].get_color():
            datos[0].set_initial_position(False)
            return "Valido"
        else:
            return "MovimientoInvalido"


    # Movimiento para el caballo    
    def movimiento_knight(chess, positions, from_row, from_col, to_row, to_col):
        pieza = positions[from_row][from_col]

        # Si la casilla destino esta ocupada por una de las piezas del mismo color, "MovimientoInvalido"
        if positions[to_row][to_col] != None and positions[to_row][to_col].get_color() == pieza.__color__:
            return "MovimientoInvalido"
        
        # Analizamos matematicantamente si el movimiento es valido
        # El desplazamiento del caballo es siempre 3 casillas
        mov_abs = abs(to_row - from_row) + abs(to_col - from_col)
        if mov_abs == 3:
            if abs(to_row - from_row) > 2 or abs(to_col - from_col) > 2:
                return "MovimientoInvalido"
            return "Valido"

        return "MovimientoInvalido"
    
    # Movimiento del Rey
    def movimiento_king(chess, positions, from_row, from_col, to_row, to_col):
        pieza = positions[from_row][from_col]

        # Si la casilla destino esta ocupada por una de las piezas del mismo color, "MovimientoInvalido"
        destination = positions[to_row][to_col]
        if destination != None and destination.get_color() == pieza.__color__:
            return "MovimientoInvalido"
        
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col
        
        #Detectamos aritmeticamente si se mueve a una casilla contigua
        if sqrt(mov_fila**2 + mov_columna**2) == 1 or sqrt(mov_fila**2 + mov_columna**2) == sqrt(2):
            return "Valido"
    

        return "MovimientoInvalido"
    
    # Movimiento de la Reina
    def movimiento_queen(chess, positions, from_row, from_col, to_row, to_col):

        mov_vertical = to_row - from_row
        mov_horizontal = to_col - from_col

        # El movimiento de la reina es basicamente el de la torre junto al del alfil
        # Detectamos si el movimiento es diagonal o perpendicular, y llamamos al metodo correspondiente
        if mov_vertical == 0  or mov_horizontal == 0:
            return chess.movimiento_perpendicular(positions, from_row, from_col, to_row, to_col)

        if mov_vertical != 0  and mov_horizontal != 0:
            return chess.movimiento_diagonal(positions, from_row, from_col, to_row, to_col)
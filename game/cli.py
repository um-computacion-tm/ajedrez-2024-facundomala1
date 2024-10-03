
from game.cheess import Chess
from game.exeptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, InvalidMove, IndexErrorPersonalizada
import os

class Cliente:
    def limpiar_consola(self):
        if os.name == 'nt':  
            os.system('cls')
        else:  
            os.system('clear')

    def inicializar_chess(self):
        # Inicialización del chess
        chess = Chess()
        tablero = chess.obtener_tablero()
        posiciones = tablero.obtener_posiciones()
        return [chess, posiciones]

    def comenzar_iteracion(self, chess, posiciones):
        print("Para salir, ingrese 999 en la fila de origen.")
        print("Turno: " + chess.obtener_turno())
        print("   " + "   ".join([str(i) for i in range(8)]))

        print("  " + "----" * 8)  

        for i, fila in enumerate(posiciones):
            fila_str = ' | '.join([str(pieza) if pieza else ' ' for pieza in fila])
            print(f'{i} | {fila_str} |')  
            print("  " + "----" * 8)  

    def funcion_entrada(self):
        from_row = int(input('Fila de origen: '))

        if from_row == 999:
            return False

        Cliente.buscar_error_indice(self, from_row)

        from_col = int(input('Columna de origen: '))
        Cliente.buscar_error_indice(self, from_col)

        to_row = int(input('Fila de destino: '))
        Cliente.buscar_error_indice(self, to_row)

        to_col = int(input('Columna de destino: '))
        Cliente.buscar_error_indice(self, to_col)   

        return [from_row, from_col, to_row, to_col]

    def buscar_error_indice(self, entrada):
        if not (0 <= entrada < 8):
            raise IndexErrorPersonalizada

    def detectar_excepcion(self, movimiento):
        if movimiento == "ColorIncorrecto":
            raise ColorIncorrecto
        if movimiento == "MismaCasilla":
            raise MismaCasilla
        if movimiento == "CasillaOcupada":
            raise CasillaOcupada
        if movimiento == "PiezaNoExiste":
            raise PiezaNoExiste
        if movimiento == "InvalidMove":
            raise InvalidMove
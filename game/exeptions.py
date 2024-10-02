#Excepciones personalizadas

class IndexErrorPersonalizada(Exception):
    def __init__(self):
        super().__init__("Numero de fila o columna incorrecto. Intentelo de nuevo.")


class CasillaOcupada(Exception):
    def __init__(self):
        super().__init__("La casilla seleccionada ya está ocupada por otra de tus piezas. Intentelo de nuevo.")


class PiezaNoExiste(Exception):
    def __init__(self):
        super().__init__("No hay pieza en esa casilla. Intentelo de nuevo.")

class MismaCasilla(Exception):
    def __init__(self):
        super().__init__("No puede mover una pieza a su misma casilla. Intentelo de nuevo.")

class ColorIncorrecto(Exception):
    def __init__(self):
        super().__init__("La pieza seleccionada no es de tu color. Intentelo de nuevo.")

class MovimientoInvalido(Exception):
    def __init__(self):
        super().__init__("El movimiento no es válido. Intentelo de nuevo.")
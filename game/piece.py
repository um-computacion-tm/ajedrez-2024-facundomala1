# Clase padre pieza 
# Abstracta

from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color):
        self.__color__ = color

    # Movimientos
    @abstractmethod
    def is_valid_movement(self, initial_row, initial_col, final_row, final_col):
        """Este método será implementado por cada pieza específica."""
        raise NotImplementedError("Este método debe ser sobreescrito en las subclases")
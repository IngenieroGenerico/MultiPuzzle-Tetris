from ..Block import GAME_COLORS
from enum import Enum

class PIECE_TYPE(Enum):
    I = 1
    J = 2
    L = 3
    O = 4
    S = 5
    T = 6
    Z = 7
    
class Piece:
    """
    Used as base class from all pieces will inheritance
    """
    def __init__(self) -> None:
        """
        Constructor where all variables and data types are create it.
        """
        self.__type = None
        self._color = None
        self._pivot = Block()
        self._blocks = []

    def setColor(self, color: GAME_COLORS) -> None:
        """
        Set color to all blocks in this piece

        Args:
            color (GAME_COLORS): Color to set it.
        """
        self._color = color
        for i in self._blocks:
            i.setColor(color)
            
    def setType(self, type: PIECE_TYPE = None) -> None:
        self.__type = type
    
    def getType(self) -> PIECE_TYPE:
        return self.__type
    
    def rotate(self) -> None:
        pass
    def update(self) -> None:
        """_summary_
        """
        pass
    def render(self) -> None:
        """_summary_
        """
        pass
    def destroy(self) -> None:
        """_summary_
        """
        pass
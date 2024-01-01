from ..Block import *

class Piece:
    """
    Used as base class from all pieces will inheritance
    """
    def __init__(self)->None:
        """
        Constructor where all variables and data types are create it.
        """
        self._color = None
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